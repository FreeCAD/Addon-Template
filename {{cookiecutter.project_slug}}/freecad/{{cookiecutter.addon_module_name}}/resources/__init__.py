# SPDX-License: CC0-1.0
# Author: Frank David Martínez Muñoz. <mnesarco at gmail.com> 2026

"""
Resource manager for the addon.

Provides the Resources class to handle icons and translations registration
with FreeCAD's GUI system. Uses importlib.resources for path resolution,
making the addon work from both regular installs and zip imports.

Usage from init_gui.py:
    from .resources import Resources
    Resources.gui_register_icons()
    Resources.gui_register_translations()
"""

import importlib
import importlib.resources
from importlib.abc import Traversable
from typing import ClassVar

import FreeCAD as App  # type: ignore


class Resources:
    """Addon {{cookiecutter.addon_name}} resource manager"""

    _pkg: ClassVar[Traversable] = importlib.resources.files(__name__)
    _gui_icons_added: ClassVar[bool] = False
    _gui_translations_added: ClassVar[bool] = False

    @classmethod
    def icon(cls, path: str) -> str:
        """Resolve relative icon path to actual path in the module system"""
        base = cls._pkg / "icons"
        return str(base.joinpath(path))

    @classmethod
    def __truediv__(cls, path: str) -> str:
        """Resolve relative resource path to actual path in the module system"""
        return str(cls._pkg.joinpath(path))

    @classmethod
    def gui_register_icons(cls) -> bool:
        if not App.GuiUp:
            msg = f"{__name__}: Icon path cannot be added without Gui."
            raise RuntimeError(msg)

        if cls._gui_icons_added:
            return

        icons = str(cls._pkg / "icons")
        App.Console.PrintLog(f"Installing {__name__}: icons={icons}\n")
        App.Gui.addIconPath(icons)
        cls._gui_icons_added = True

    @classmethod
    def gui_register_translations(cls) -> bool:
        if not App.GuiUp:
            msg = f"{__name__}: Translations path cannot be added without Gui."
            raise RuntimeError(msg)

        if cls._gui_translations_added:
            return

        translations = str(cls._pkg / "translations")
        App.Console.PrintLog(f"Installing {cls.__qualname__}: translations={translations}\n")
        App.Gui.addLanguagePath(translations)
        App.Gui.updateLocale()
        cls._gui_translations_added = True
