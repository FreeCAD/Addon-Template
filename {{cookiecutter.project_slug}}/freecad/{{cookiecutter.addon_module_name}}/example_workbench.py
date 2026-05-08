# SPDX-License-Identifier: {{ cookiecutter.addon_license }}

"""Example FreeCAD Workbench."""

import FreeCAD as App
import FreeCADGui as Gui

from PySide.QtCore import QT_TRANSLATE_NOOP

from .resources import Resources
from .commands import ExampleCommand

class {{ cookiecutter.addon_name }}Workbench(Gui.Workbench):

    MenuText: str = QT_TRANSLATE_NOOP(
            "{{ cookiecutter.addon_module_name }}",
            "Example Workbench",
        )

    ToolTip: str = QT_TRANSLATE_NOOP(
            "{{ cookiecutter.addon_module_name }}",
            "Example Workbench tooltip",
        )

    Icon: str = Resources.icon("{{ cookiecutter.__addon_icon_filename }}-wb.svg")


    def Initialize(self) -> None:
        App.Console.PrintMessage("Example Workbench initialized\n")
        # Adding menus and toolbars when the Workbench is active (example)
        commands = [ExampleCommand.Name]
        self.appendToolbar("{{ cookiecutter.addon_name }}", commands)
        self.appendMenu("{{ cookiecutter.addon_name }}", commands)

    def Activated(self) -> None:
        App.Console.PrintMessage("Example Workbench activated\n")

    def Deactivated(self) -> None:
        App.Console.PrintMessage("Example Workbench deactivated\n")

    def ContextMenu(self, recipient: str) -> None:
        App.Console.PrintMessage("Example Workbench context menu\n")
        # Adding context menus when the Workbench is active (example)
        self.appendContextMenu("", [ExampleCommand.Name])

    @classmethod
    def Install(cls) -> None:
        Gui.addWorkbench(cls)
