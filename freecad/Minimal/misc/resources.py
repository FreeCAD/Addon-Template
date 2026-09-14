# SPDX-License-Identifier: CC0-1.0
# SPDX-FileNotice: Part of the Minimal addon.

from importlib.resources import as_file, files

import freecad.Minimal as module

resources = files(module) / "resources"
icons = resources / "icons"


def as_icon(name: str) -> str:
    icon = icons / (name + ".svg")
    with as_file(icon) as path:
        return str(path)
