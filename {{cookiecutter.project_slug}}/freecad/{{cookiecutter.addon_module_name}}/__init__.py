# SPDX-License-Identifier: {{ cookiecutter.addon_license }}

"""
Entry point for the addon (headless mode).

This file is loaded once during FreeCAD initialization if the addon is not disabled.
It runs in headless mode, so no Gui imports or calls are allowed here.

FreeCAD discovers addons using the native namespace package structure:
    freecad/<module_name>/

The parent `freecad/` package uses native namespace packaging (no __init__.py),
allowing multiple addons to coexist under the same freecad namespace.

Loading sequence:
    1. FreeCAD imports freecad.<module_name> (this file) during startup
    2. If FreeCAD is running with GUI, it later imports init_gui.py in the same package
    3. GUI-related code (workbenches, toolbars, etc.) belongs in init_gui.py

Keep this file fast - it runs on every FreeCAD startup.
"""
