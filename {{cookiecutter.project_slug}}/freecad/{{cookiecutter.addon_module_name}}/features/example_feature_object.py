# SPDX-License-Identifier: {{ cookiecutter.addon_license }}

"""
Basic FeaturePythonObject example.

see: https://wiki.freecad.org/Scripted_objects
see: https://wiki.freecad.org/App_FeaturePython
"""

from __future__ import annotations

import FreeCAD as App

class MyCoolCube:
    """
    Cool Box to demonstrate basic FPO.
    """

    def __init__(self, obj: App.DocumentObject) -> None:
        """Add some custom properties to our box feature"""
        obj.addProperty("App::PropertyLength", "Length", "Box", "Length of the box").Length = 1.0
        obj.addProperty("App::PropertyLength", "Width", "Box", "Width of the box").Width = 1.0
        obj.addProperty("App::PropertyLength", "Height", "Box", "Height of the box").Height = 1.0
        obj.Proxy = self

    def onChanged(self, obj: App.DocumentObject, prop: str) -> None:
        """Do something when a property has changed"""
        App.Console.PrintMessage("Change property: " + str(prop) + "\n")

        # Eager recompute on change (optional)
        if prop in ("Length", "Width", "Height"):
            self.execute(obj)

    def execute(self, obj: App.DocumentObject) -> None:
        """Do something when doing a recomputation, this method is mandatory"""
        import Part
        App.Console.PrintMessage("Recompute Python Box feature\n")
        obj.Shape = Part.makeBox(obj.Length, obj.Width, obj.Height)

    @classmethod
    def create(cls, name: str | None = None, doc: App.Document | None = None) -> MyCoolCube:
        """Optional utility method to create instances of this feature"""

        # Check valid document
        if not (doc := doc or App.ActiveDocument):
            raise ValueError("A FreeCAD document is required")

        # Create the c++ DocumentObject
        # see: https://wiki.freecad.org/App_FeaturePython
        obj = doc.addObject("Part::FeaturePython", name or "MyCoolBox")

        # Bind the Python Proxy
        proxy = cls(obj)

        # Manage Gui (ViewProvider) if available
        if App.GuiUp and hasattr(obj, "ViewObject"):
            from .example_feature_vp import MyCoolCubeViewProvider
            MyCoolCubeViewProvider(obj.ViewObject)

        obj.recompute()
        return proxy