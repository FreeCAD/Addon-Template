# SPDX-License-Identifier: {{ cookiecutter.addon_license }}

"""
Basic ViewProvider example.

see: https://wiki.freecad.org/Scripted_objects
"""

from __future__ import annotations
from ..resources import Resources

import FreeCADGui as Gui


class MyCoolCubeViewProvider:
    """
    Basic ViewProvider with custom Icon.
    """

    def __init__(self, obj: Gui.ViewProviderDocumentObject) -> None:
        obj.Proxy = self

    def getIcon(self) -> str:
        return Resources.icon("{{ cookiecutter.__addon_icon_filename }}.svg")
