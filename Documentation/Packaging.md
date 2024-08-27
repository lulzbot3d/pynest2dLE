
# Packaging

*Creating a new **PyNest2DLE** Conan package so it can be used in **CuraLE** and **UraniumLE**.*

Run the following

```shell
conan create .                                \
    pynest2dle/<version>@<username>/<channel> \
    --build=missing                           \
    --update
```

This package will be stored in the local Conan cache.

`~/.conan/data` or `C:\Users\username\.conan\data`

It can be used in downstream projects, such as **CuraLE** and **UraniumLE** by adding it as a requirement in the `conanfile.py` or in `conandata.yml`.

*Make sure that the used `<version>` is present in the `conandata.yml` in the PyNest2D root.*

You can also specify the override at the commandline, to use the newly created package, when you execute the install command in the root of the consuming project.

```shell
conan install .     \
    -build=missing  \ 
    --update        \
    --require-override=pynest2dle/<version>@<username>/<channel>
```
