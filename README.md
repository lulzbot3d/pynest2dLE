# PyNest2DLE

[![Badge Conan]][Conan]

[![Badge Size]][Size]
[![Badge License]][License]

*CPython bindings for **[LibNest2D]**, a library
to pack 2D polygons into a small space.*

[![Button Requirements]][Requirements]
[![Button Usage]][Usage]
[![Button Building]][Building]
[![Button Packaging]][Packaging]
[![Button Developing]][Developing]

## Details

> Note:  
> The following is regarding the UltiMaker repository, this may not all apply to the code being used in this LulzBot fork.

We may use as of yet unmerged work done on our own **[Fork]** of libnest2d whenever convenient.

Libnest2d implements the 2D bin packing problem.

The objective of this repository is to allow libnest2d functions to be called from Python using Numpy.

To this end, there is a competing **[solution][Nest2D]** to provide Python bindings.

However it doesn't expose enough of the configurability that Cura requires and its bindings aren't as transparent.

<!----------------------------------------------------------------------------->

[LibNest2D]: https://github.com/tamasmeszaros/libnest2d
[Nest2D]: https://github.com/markfink/nest2D
[Conan]: https://github.com/lulzbot3d/pynest2dLE/actions/workflows/conan-package.yml
[Fork]: https://github.com/lulzbot3d/libnest2dLE

[Requirements]: Documentation/System%20Requirements.md
[Developing]: Documentation/Developing.md
[Packaging]: Documentation/Packaging.md
[Building]: Documentation/Building.md
[Usage]: Documentation/Usage.md
[License]: LICENSE
[Size]: https://github.com/lulzbot3d/pynest2dLE

<!---------------------------------[ Badges ]---------------------------------->

[Badge Conan]: https://img.shields.io/github/actions/workflow/status/lulzbot3d/pynest2dLE/conan-package.yml?style=for-the-badge&color=C1D82F&labelColor=788814&logoColor=white&logo=conan&label=Conan%20Package
[Badge Size]: https://img.shields.io/github/repo-size/lulzbot3d/pynest2dLE?style=for-the-badge&color=CCCCCC&labelColor=666666&logoColor=white&logo=GoogleAnalytics
[Badge License]: https://img.shields.io/badge/License-LGPL3-336887.svg?style=for-the-badge&color=A32D2A&labelColor=511615&logoColor=white&logo=GNU

<!---------------------------------[ Buttons ]--------------------------------->

[Button Requirements]: https://img.shields.io/badge/System_Requirements-c34360?style=for-the-badge&logoColor=white&logo=BookStack
[Button Developing]: https://img.shields.io/badge/Developing-715a97?style=for-the-badge&logoColor=white&logo=VisualStudioCode
[Button Packaging]: https://img.shields.io/badge/Packaging-db5e8a?style=for-the-badge&logoColor=white&logo=GitLFS
[Button Building]: https://img.shields.io/badge/Building-458cb5?style=for-the-badge&logoColor=white&logo=CurseForge
[Button Usage]: https://img.shields.io/badge/Usage-629944?style=for-the-badge&logoColor=white&logo=GitBook

