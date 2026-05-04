# FreeCAD Addon Template

CookieCutter template for generating FreeCAD addons. NOTE: You do not need to fork this template to use it, just follow the "Quick Start" instructions below.

## Dependencies

* uv: https://docs.astral.sh/uv/

## Quick Start

### Install uv

Typically one line:
```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

More methods: https://docs.astral.sh/uv/getting-started/installation/

### Create an addon

Launch cookiecutter and point it at the template repo:

```shell
uvx cookiecutter https://github.com/FreeCAD/Addon-Template.git --checkout cookie
```

Answer the questions:

```shell
  [1/13] Addon name (MyAddon):
  [2/13] Project directory (MyAddon):
  [3/13] Python sub-module name (MyAddon):
  [4/13] Name of the svg icon file (addon.svg):
  [5/13] Name of the author/maintainer (me):
  [6/13] Email of the author/maintainer (me@foobar.com):
  [7/13] Short description of the addon (MyAddon does something cool.):
  [8/13] Required pypi dependencies (optional, separated by comma. i.e. numpy,pillow) ():
  [9/13] Initial version using format major.minor.review (0.1.0):
  [10/13] Select addon_license
    1 - LGPL-2.1-or-later
    2 - LGPL-3.0-or-later
    3 - GPL-3.0-or-later
    4 - MIT
    5 - CC0
    6 - CC-BY-SA-4.0
    7 - OTHER
    Choose from [1/2/3/4/5/6/7] (1):
  [11/13] Select assets_license
    1 - CC-BY-SA-4.0
    2 - CC0
    3 - LGPL-2.1-or-later
    4 - LGPL-3.0-or-later
    5 - GPL-3.0-or-later
    6 - MIT
    7 - OTHER
    Choose from [1/2/3/4/5/6/7] (1):
  [12/13] Full url of the git repository (https://github.com/me/MyAddon):
  [13/13] Name of the default git branch (main):
```

Voila, the addon has been created in a directory under the current directory:

```shell
$ tree MyAddon/
```

Shows...

```shell
MyAddon
├── freecad
│   └── MyAddon
│       ├── commands
│       │   ├── example_command.py
│       │   └── __init__.py
│       ├── init_gui.py
│       ├── __init__.py
│       ├── resources
│       │   ├── icons
│       │   │   └── addon.svg
│       │   ├── __init__.py
│       │   ├── translations
│       │   │   ├── MyAddon_es-ES.ts
│       │   │   ├── README.md
│       │   │   └── update_translation.py
│       │   └── ui
│       └── version.py
├── LICENSE-Assets
├── LICENSE-Code
├── package.xml
├── pyproject.toml
└── README.md
```

### Install the addon

The easiest way (I've found) to install a newly created addon is to just symlink it into the `Mod` directory.

```bash
# cd to the Mod directory of your FreeCAD installation]
cd <FreeCAD user's config directory>/Mod
ln -s <path to the created addon> MyAddon
```

### Testing the addon without installing it

```shell
freecad -M <path to MyAddon>
```

## For Installation into the AddOnManager

See instructions here:
https://freecad.github.io/Addon-Academy/


## Contributors

This template summarizes work from previous templates created by:

* @looooo
* @ToddG
* @PhoneDroid
* @mnesarco

