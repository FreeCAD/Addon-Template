<!-- SPDX-License-Identifier: CC0-1.0 -->
<!-- SPDX-FileNotice: Part of the Minimal addon. -->

# Contributing

How to contribute to this addon.

## TLDR

- Standard PR based workflow.
- For new files add SPDX or license metadata for icons.
- Open an issue for larger stuff.

## Setup

- Fork & clone the repository.
- Using [uv], install the dev dependencies:

  ```sh
  uv sync
  ```

- Link the cloned repository folder to your FreeCAD `/Mod/` directory.

## Release

1. Bump the `<version>` & `<date>` tags in the manifest.
2. Create a GitHub release + tag and describe your changes.
3. Add an entry into the `CHANGELOG.md` file for the release.
4. If the `<freecadmin>` version changed, open an issue on the [Index] repository to request a backwards compatibility entry.

[Index]: https://github.com/FreeCAD/Addons
[uv]: https://docs.astral.sh/uv/
