# SPDX-License-Identifier: {{ cookiecutter.addon_license }}

"""
{{ cookiecutter.addon_name }} Command Module

Commands in FreeCAD are the primary way to expose functionality to the user through
toolbar buttons, menu items, or direct invocation via FreeCADGui.runCommand().

Each command is a Python class that must implement:
    - GetResources(): Returns a dict with 'Pixmap' (icon path), 'MenuText',
      'ToolTip', and optionally 'Accel' (keyboard shortcut). Use QT_TRANSLATE_NOOP
      for translatable strings.
    - Activated(): Called when the command is triggered (button press or shortcut).
    - IsActive(): Returns True if the command is available, False to grey it out.

Commands are registered with FreeCADGui.addCommand(name, commandObject) where name
must be a unique string (typically 'WorkbenchName_CommandName'). Registration is
usually done in init_gui.py or the workbench's Initialize() method.

Commands only work in GUI mode and are typically defined per workbench. For scriptable
operations, consider providing a corresponding Python function alongside the command.

Example:
    class MyCommand:
        def GetResources(self):
            return {'Pixmap': 'MyCommand.svg',
                    'MenuText': QT_TRANSLATE_NOOP("{{ cookiecutter.addon_name }}", "My Command"),
                    'ToolTip': QT_TRANSLATE_NOOP("{{ cookiecutter.addon_name }}", "Description")}

        def Activated(self):
            print("Command activated")

        def IsActive(self):
            return True

    FreeCADGui.addCommand("My_Command", MyCommand())

Notice:
    Adding commands with FreeCADGui.addCommand(...) does not create Menus or Toolbar actions automatically.
    Once the command is added, it can be used via FreeCADGui.runCommand().
    To create actual Gui menus/toolbars etc.. you need to implement a Workbench or a Workbench Manipulator or
    use direct Qt (PySide) api.

Good practices:
    - define each command in its own python module
    - Always add commands prefixed by Addon name or Addon name abbr
    - Only add commands when Gui is Up
    - Do not change command names as it will break macros referencing them
    - Export command classes here it to make it explicit public
"""

from .example_command import ExampleCommand as ExampleCommand
from .example_manipulator import WorkbenchManipulator as WorkbenchManipulator
