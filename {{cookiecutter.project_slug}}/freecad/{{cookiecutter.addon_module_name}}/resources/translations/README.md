# About translating {{cookiecutter.addon_module_name}}

> [!NOTE]
> All commands **must** be run in `./freecad/{{cookiecutter.addon_module_name}}/resources/translations/` directory.

> [!IMPORTANT]
> The translation tools (`lupdate`, `lrelease`, and `linguist`) are provided by **PySide6**,
> which is installed as a dev dependency. Use `uv run` to execute the script
> within the uv-managed environment.

## Updating translations template file

To update the template file from source files you should use this command:

```shell
uv run python update_translation.py -U
```

Once done you can commit the changes and upload the new file to CrowdIn platform
at <https://crowdin.com/project/freecad-addons> webpage and find the **{{cookiecutter.addon_module_name}}** project.

## Creating file for missing locale

To create a file for a new language with all **{{cookiecutter.addon_module_name}}** translatable strings execute
the script with `-u` flag plus your locale:

```shell
uv run python update_translation.py -u ja
```

To update the main translation file and all locale-specific files at once:

```shell
uv run python update_translation.py -A
```

The supported locales are (from `FreeCADGui.supportedLocales()`):

```python
{"en", "af", "ar", "eu", "be", "bg", "ca", "zh-CN", "zh-TW", "hr",
"cs", "da", "nl", "fil", "fi", "fr", "gl", "ka", "de", "el", "hu",
"id", "it", "ja", "kab", "ko", "lt", "no", "pl", "pt-PT", "pt-BR",
"ro", "ru", "sr", "sr-CS", "sk", "sl", "es-ES", "es-AR", "sv-SE",
"tr", "uk", "val-ES", "vi"}
```

## Translating

To edit your language file open your file in Qt Linguist (installed with PySide6)
or in a text editor like `xed`, `mousepad`, `gedit`, `nano`, `vim`/`nvim`,
`geany` etc. and translate it.

You can also open the locale directly in Qt Linguist using the script:

```shell
uv run python update_translation.py -l ja
```

Alternatively you can visit the **FreeCAD-addons** project on CrowdIn platform
at <https://crowdin.com/project/freecad-addons> webpage and find your language,
once done, look for the **{{cookiecutter.addon_module_name}}** project.

## Compiling translations

To convert all `.ts` files to `.qm` files (merge) you can use this command:

```shell
uv run python update_translation.py -R
```

If you are a translator that wants to update only their language file
to test it on **FreeCAD** before doing a PR you can use this command:

```shell
uv run python update_translation.py -r ja
```

This will update the `.qm` file for your language (Japanese in this case).

## Sending translations

Now you can contribute your translated `.ts` file to **{{cookiecutter.addon_module_name}}** repository,
also include the `.qm` file.

<{{cookiecutter.addon_repo_url}}>

## More information

You can read more about translating external workbenches here:

<https://wiki.freecad.org/Translating_an_external_workbench>
