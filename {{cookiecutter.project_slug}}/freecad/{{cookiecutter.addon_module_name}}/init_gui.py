"""
GUI entry point for the addon.

This file is imported by FreeCAD after __init__.py when the GUI is available.
It runs only in GUI mode and is the place for GUI-related initialization:
registering workbenches, toolbars, menus, and loading icons/translations.

FreeCAD loading sequence:
    1. freecad.<module_name>.__init__.py (headless, always runs)
    2. freecad.<module_name>.init_gui.py (GUI only, runs when GUI is available)

Keep this file fast - it runs on every FreeCAD GUI startup.
"""

from .resources import Resources
from .commands import ExampleCommand

# Install icons (optional)
Resources.gui_register_icons()

# Install translations (if any)
Resources.gui_register_translations()

# Install commands
ExampleCommand.Install()