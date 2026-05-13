from pathlib import Path

path = Path()

banner = f"""

═════════════════════════════════════════════════════════
                 -= Project created =-

Your new Addon directory has been created:
{path.absolute()!s}

For more information about FreeCAD Addon development, see the Addon Academy at
https://freecad.github.io/Addon-Academy/

"""

if __name__ == "__main__":
    print(banner)
