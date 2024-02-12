import os

from pathlib import Path
from os import path

from conan import ConanFile
from conan.errors import ConanInvalidConfiguration
from conan.tools.build import check_min_cppstd
from conan.tools.cmake import CMake, CMakeToolchain, cmake_layout, CMakeDeps
from conan.tools.files import copy, mkdir, update_conandata
from conan.tools.microsoft import check_min_vs, is_msvc, is_msvc_static_runtime
from conan.tools.scm import Version, Git

required_conan_version = ">=1.58.0"


class PyNest2DConan(ConanFile):
    name = "pynest2d"
    license = "LGPL-3.0"
    author = "Ultimaker B.V."
    url = "https://github.com/Ultimaker/pynest2d"
    description = "Python bindings for libnest2d"
    topics = ("conan", "cura", "prusaslicer", "nesting", "c++", "bin packaging", "python", "sip")
    settings = "os", "compiler", "build_type", "arch"
    exports = "LICENSE*"
    package_type = "library"

    python_requires = "pyprojecttoolchain/[>=0.2.0]@ultimaker/cura_11622", "sipbuildtool/[>=0.3.0]@ultimaker/cura_11622"  # FIXME: use stable after merge

    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "py_build_requires": ["ANY"],
        "py_build_backend": ["ANY"],
    }
    default_options = {
        "shared": True,
        "fPIC": True,
        "py_build_requires": '"sip >=6, <7", "setuptools>=40.8.0", "wheel"',
        "py_build_backend": "sipbuild.api",
    }

    def set_version(self):
        if not self.version:
            self.version = self.conan_data["version"]

    def export(self):
        git = Git(self)
        update_conandata(self, {"version": self.version, "commit": git.get_commit()})

    @property
    def _min_cppstd(self):
        return 17

    @property
    def _compilers_minimum_version(self):
        return {
            "gcc": "9",
            "clang": "9",
            "apple-clang": "9",
            "msvc": "192",
            "visual_studio": "14",
        }

    def export_sources(self):
        copy(self, "CMakeLists.txt", self.recipe_folder, self.export_sources_folder)
        copy(self, "*", path.join(self.recipe_folder, "python"), path.join(self.export_sources_folder, "python"))

    def requirements(self):
        for req in self.conan_data["requirements"]:
            self.requires(req)

    def validate(self):
        if self.settings.compiler.cppstd:
            check_min_cppstd(self, self._min_cppstd)
        check_min_vs(self, 192)  # TODO: remove in Conan 2.0
        if not is_msvc(self):
            minimum_version = self._compilers_minimum_version.get(str(self.settings.compiler), False)
            if minimum_version and Version(self.settings.compiler.version) < minimum_version:
                raise ConanInvalidConfiguration(
                    f"{self.ref} requires C++{self._min_cppstd}, which your compiler does not support."
                )

    def build_requirements(self):
        self.test_requires("standardprojectsettings/[>=0.2.0]@ultimaker/cura_11622")  # FIXME: use stable after merge
        self.test_requires("sipbuildtool/[>=0.3.0]@ultimaker/cura_11622")  # FIXME: use stable after merge
        self.test_requires("cpython/3.12.2@ultimaker/cura_11622")  # FIXME: use stable after merge

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")
        self.options["cpython"].shared = True

    def generate(self):
        tc = self.python_requires["pyprojecttoolchain"].module.PyProjectToolchain(self)
        tc.blocks["tool_sip_project"].values["sip_files_dir"] = str(Path("python").as_posix())
        tc.blocks.remove("extra_sources")
        tc.generate()

        tc = CMakeDeps(self)
        tc.generate()

        tc = CMakeToolchain(self)
        if is_msvc(self):
            tc.variables["USE_MSVC_RUNTIME_LIBRARY_DLL"] = not is_msvc_static_runtime(self)
        tc.cache_variables["CMAKE_POLICY_DEFAULT_CMP0148"] = "OLD"
        cpython_conf = self.dependencies["cpython"].conf_info
        tc.variables["Python_EXECUTABLE"] = cpython_conf.get("user.cpython:python").replace("\\", "/")
        tc.variables["Python_ROOT_DIR"] = cpython_conf.get("user.cpython:python_root").replace("\\", "/")
        cpython_options = self.dependencies["cpython"].options
        tc.variables["Python_USE_STATIC_LIBS"] = not cpython_options.shared
        tc.variables["Python_FIND_FRAMEWORK"] = "NEVER"
        tc.variables["Python_FIND_REGISTRY"] = "NEVER"
        tc.variables["Python_FIND_IMPLEMENTATIONS"] = "CPython"
        tc.variables["Python_FIND_STRATEGY"] = "LOCATION"
        tc.variables["Python_SITEARCH"] = "site-packages"
        tc.generate()

        # Generate the Source code from SIP
        tc = self.python_requires["sipbuildtool"].module.SipBuildTool(self)
        tc.configure()
        tc.build()

    def layout(self):
        cmake_layout(self)

        if self.settings.os in ["Linux", "FreeBSD", "Macos"]:
            self.cpp.package.system_libs = ["pthread"]

        self.cpp.package.lib = ["pySavitar"]
        self.cpp.package.libdirs = ["lib"]

        self.layouts.build.runenv_info.prepend_path("PYTHONPATH", ".")
        self.layouts.package.runenv_info.prepend_path("PYTHONPATH", "lib")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        copy(self, pattern="LICENSE*", dst="licenses", src=self.source_folder)
        for ext in ("*.pyi", "*.so", "*.lib", "*.a", "*.pyd", "*.dll", "*.dylib"):
            copy(self, ext, src=self.build_folder, dst=path.join(self.package_folder, "lib"), keep_path=False)

    def package_info(self):
        self.conf_info.define("user.pysavitar:pythonpath", os.path.join(self.package_folder, "lib"))
