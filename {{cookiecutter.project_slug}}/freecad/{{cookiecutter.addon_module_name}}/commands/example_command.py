# SPDX-License-Identifier: {{ cookiecutter.addon_license }}

"""Example FreeCAD command demonstrating the command structure."""

import FreeCAD as App
from PySide.QtCore import QT_TRANSLATE_NOOP

from ..resources import Resources


class ExampleCommand:
    """Example command that demonstrates the FreeCAD command structure."""

    def __init__(self) -> None:
        # Optional: initialize instance variables that persist for the command's lifetime
        pass

    def GetResources(self) -> dict[str, str]:
        # Returns a dictionary that defines how the command appears in the UI.
        # - Pixmap: path to the icon file (relative to FreeCAD's icon search paths or absolute path)
        # - MenuText: text shown in menus (use QT_TRANSLATE_NOOP for translation support)
        # - ToolTip: text shown when hovering over the button/menu item
        # - Accel: optional keyboard shortcut (e.g., "Ctrl+A")
        return {
            "Pixmap": Resources.icon(
                "{{ cookiecutter.__addon_icon_filename }}.svg"
            ),
            "MenuText": QT_TRANSLATE_NOOP(
                "{{ cookiecutter.addon_module_name }}_Example",
                "Example Command",
            ),
            "ToolTip": QT_TRANSLATE_NOOP(
                "{{ cookiecutter.addon_module_name }}_Example",
                "Runs the example command",
            ),
        }

    def Activated(self) -> None:
        # Called when the user triggers the command (clicks the toolbar button,
        # selects the menu item, or runs FreeCADGui.runCommand()).
        # Place the main logic of your command here.
        App.Console.PrintMessage("Example Command activated\n")

    def IsActive(self) -> bool:
        # Called frequently by FreeCAD to determine if the command should be
        # enabled (True) or greyed out/disabled (False).
        # Use this to check for conditions like: active document exists,
        # objects are selected, workbench is in correct state, etc.
        return True

    @classmethod
    def Install(cls) -> None:
        # Optional utility method to register the command
        if App.GuiUp:
            App.Gui.addCommand(
                "{{ cookiecutter.addon_module_name }}_ExampleCommand", cls()
            )
