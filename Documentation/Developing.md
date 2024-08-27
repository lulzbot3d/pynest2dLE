
# Developing PyNest2DLE In Editable Mode

You can use your local development repository downsteam by adding it as an editable mode package, which also means that you can test it in a consuming project without creating a new package for this project every time.

```shell
conan editable add . \
    pynest2dle/<version>@<username>/<channel>
```

Then in your downsteam project's (such as CuraLE) root directory, override the package with your editable mode package.

```shell
conan install .     \
    -build=missing  \
    --update        \
    --require-override=pynest2dle/<version>@<username>/<channel>
```
