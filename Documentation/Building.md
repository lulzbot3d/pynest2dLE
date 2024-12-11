
# Building

> We are currently in the process of switch our builds and pipelines to an approach which uses **[Conan]** and pip to manage our dependencies, which are stored on our **JFrog Artifactory** server and in the pypi.org. *Not everything has been fully ported yet, so bare with us.*

## Related

**[Conan]** is a Python program and can be installed using pip. If you have never used it read their **[Documentation][Conan Docs]** which is quite extensive and well maintained.

## Configuring Conan

```shell
pip install conan --upgrade
conan config install https://github.com/lulzbot3d/conan-config-le.git
conan profile new default --detect --force
```

Community developers would have to remove the Conan cura-le repository because it requires credentials.

LulzBot developers need to request an account for our JFrog Artifactory server with IT.

```shell
conan remote remove cura-le
```

## Clone PyNest2DLE

```shell
git clone https://github.com/lulzbot3d/pynest2dLE.git
cd pynest2dLE
```

## Building & Installation

### Release

```shell
conan install . --build=missing --update
# optional for a specific version: conan install . pynest2d/<version>@<user>/<channel> --build=missing --update
conan build .
```

or alternatively:

```shell
sip-install
```

### Debug

```shell
conan install . --build=missing --update build_type=Debug
conan build .
```

or alternatively:

```shell
sip-install
```

<!----------------------------------------------------------------------------->

[Conan Docs]: https://docs.conan.io/en/latest/index.html
[Conan]: https://conan.io/
