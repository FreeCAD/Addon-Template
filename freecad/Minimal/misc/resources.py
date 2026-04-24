# SPDX-License-Identifier: LGPL-3.0-or-later
# SPDX-FileNotice: Part of the Minimal addon.

import freecad.Minimal as module
from importlib.resources import as_file, files

resources = files(module) / 'Resources'
icons = resources / 'Icons'


def as_icon(name: str) -> str:
    icon = icons / (name + '.svg')
    with as_file(icon) as path:
        return str(path)
