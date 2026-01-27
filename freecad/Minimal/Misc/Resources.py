# SPDX-License-Identifier: LGPL-3.0-or-later
# SPDX-FileNotice: Part of the Minimal addon.

import freecad.Minimal as module
from importlib import resources


icons = resources.files(module) / 'Resources/Icons'


def asIcon ( name : str ):

    file = name + '.svg'

    icon = icons / file

    with resources.as_file(icon) as path:
        return str( path )
