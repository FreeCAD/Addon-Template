# SPDX-License: CC0-1.0

"""
Create, update and release translation files.

Uses lupdate and lrelease from PySide6 (installed in the uv environment).

Usage:
    uv run python update_translation.py [-R] [-U] [-A] [-r <locale>] [-u <locale>] [-l <locale>]
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

EPILOG = """
Examples:
  Update main translation file:
    uv run python update_translation.py -U

  Update main and all locales:
    uv run python update_translation.py -A

  Update and translate Spanish locale:
    uv run python update_translation.py -u es-ES

  Open Spanish locale in Qt Linguist:
    uv run python update_translation.py -l es-ES

  Release a specific locale:
    uv run python update_translation.py -r es-ES

  Release all locales:
    uv run python update_translation.py -R
"""

# Supported locales (from FreeCAD's FreeCADGui.supportedLocales())
SUPPORTED_LOCALES = {
    "en",
    "af",
    "ar",
    "eu",
    "be",
    "bg",
    "ca",
    "zh-CN",
    "zh-TW",
    "hr",
    "cs",
    "da",
    "nl",
    "fil",
    "fi",
    "fr",
    "gl",
    "ka",
    "de",
    "el",
    "hu",
    "id",
    "it",
    "ja",
    "kab",
    "ko",
    "lt",
    "no",
    "pl",
    "pt-PT",
    "pt-BR",
    "ro",
    "ru",
    "sr",
    "sr-CS",
    "sk",
    "sl",
    "es-ES",
    "es-AR",
    "sv-SE",
    "tr",
    "uk",
    "val-ES",
    "vi",
}

# Addon module name (replaced by Cookiecutter)
ADDON_NAME = "{{cookiecutter.addon_module_name}}"


def print_err(*args, **kwargs) -> None:
    """Print to stderr."""
    kwargs["file"] = sys.stderr
    print(*args, **kwargs)


def find_tools() -> tuple[str, str, str]:
    """Find lupdate and lrelease in the current environment (uv)."""
    lupdate = shutil.which("pyside6-lupdate")
    lrelease = shutil.which("pyside6-lrelease")
    linguist = shutil.which("pyside6-linguist")

    if not lupdate or not lrelease:
        print_err(
            "Error: lupdate or lrelease not found. Ensure PySide6 is installed (uv add --dev PySide6).",
        )
        sys.exit(1)
    return lupdate, lrelease, linguist


def fix_ts_locale(ts_file: Path) -> None:
    """Replace hyphens with underscores in the third line of TS files (language field)."""
    try:
        content = ts_file.read_text(encoding="utf-8")
        lines = content.splitlines(keepends=True)
        if len(lines) >= 3 and "-" in lines[2]:
            lines[2] = lines[2].replace("-", "_")
            ts_file.write_text("".join(lines), encoding="utf-8")
            print_err(f"Fixed hyphens in {ts_file}: line 3 updated")
    except Exception as e:
        print_err(f"Warning: Failed to fix {ts_file}: {e}")


def update_locale(lupdate_path: str, locale: str | None = None) -> None:
    """Update translation files using lupdate."""
    py_files = [str(p) for p in Path("../../").glob("*.py")]
    ui_files = [str(p) for p in Path("../ui/").glob("*.ui")]
    files = py_files + ui_files

    if not files:
        print_err("No Python or UI files found to update.")
        return

    if locale is None:
        ts_file = Path(f"{ADDON_NAME}.ts")
        action = "Creating" if not ts_file.exists() else "Updating"
        print(f"\n\t<<< {action} '{ts_file}' file >>>\n")
        cmd = [lupdate_path] + files + ["-ts", str(ts_file)]
    else:
        ts_file = Path(f"{ADDON_NAME}_{locale}.ts")
        action = "Creating" if not ts_file.exists() else "Updating"
        print(f"\n\t<<< {action} '{ts_file}' file >>>\n")
        target_locale = locale.replace("-", "_")
        cmd = [
            lupdate_path,
            *files,
            "-source-language",
            "en",
            "-target-language",
            target_locale,
            "-ts",
            str(ts_file),
        ]

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print_err(f"Error running lupdate: {e}")
        sys.exit(1)

    fix_ts_locale(ts_file)


def release_locale(lrelease_path: str, ts_file: Path) -> None:
    """Release a TS file to QM using lrelease."""
    if not ts_file.exists():
        print_err(f"Error: {ts_file} not found.")
        return
    print(f"Releasing {ts_file}...")
    try:
        subprocess.run([lrelease_path, str(ts_file)], check=True)
    except subprocess.CalledProcessError as e:
        print_err(f"Error running lrelease: {e}")
        sys.exit(1)


def release_all(lrelease_path: str) -> None:
    """Release all locale-specific TS files."""
    for ts_file in Path(".").glob(f"{ADDON_NAME}_*.ts"):
        release_locale(lrelease_path, ts_file)


def update_main(lupdate_path: str) -> None:
    """Update the main (locale-agnostic) TS file."""
    update_locale(lupdate_path, locale=None)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Create, update and release translation files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=EPILOG,
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-R",
        action="store_true",
        help="Release all locales",
    )
    group.add_argument(
        "-U",
        action="store_true",
        help="Update main translation file (locale agnostic)",
    )
    group.add_argument(
        "-A",
        action="store_true",
        help="Update main and all locale translation files",
    )
    group.add_argument(
        "-r",
        metavar="LOCALE",
        help="Release the specified locale",
    )
    group.add_argument(
        "-u",
        metavar="LOCALE",
        help="Update strings for the specified locale (updates main + locale)",
    )
    group.add_argument(
        "-l",
        metavar="LOCALE",
        help="Open locale in Qt Linguist for translation",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    lupdate, lrelease, linguist = find_tools()

    if args.R:
        release_all(lrelease)
    elif args.A:
        update_main(lupdate)
        prefix = f"{ADDON_NAME}_"
        for ts_file in Path(".").glob(f"{prefix}*.ts"):
            locale = ts_file.stem.removeprefix(prefix)
            update_locale(lupdate, locale)
    elif args.U:
        update_main(lupdate)
    elif args.r:
        locale = args.r
        if locale not in SUPPORTED_LOCALES:
            print_err(f"Unsupported locale: {locale}")
            print_err("Supported locales:")
            for loc in sorted(SUPPORTED_LOCALES):
                print_err(f"  {loc}")
            sys.exit(1)
        ts_file = Path(f"{ADDON_NAME}_{locale}.ts")
        release_locale(lrelease, ts_file)
    elif args.u:
        locale = args.u
        if locale not in SUPPORTED_LOCALES:
            print_err(f"Unsupported locale: {locale}")
            print_err("Supported locales:")
            for loc in sorted(SUPPORTED_LOCALES):
                print_err(f"  {loc}")
            sys.exit(1)
        update_main(lupdate)
        update_locale(lupdate, locale)
    elif args.l:
        locale = args.l
        ts_file = Path(f"{ADDON_NAME}_{locale}.ts")
        if not ts_file.exists():
            print_err(f"Error: {ts_file} not found.")
            sys.exit(1)
        if not linguist:
            print_err(
                "Warning: linguist not found. Ensure PySide6 is installed (uv add --dev PySide6)."
            )
            print_err(f"To open manually: pyside6-linguist {ts_file}")
        else:
            print(f"Opening {ts_file} in Qt Linguist...")
            subprocess.run([linguist, str(ts_file)])
    else:
        parse_args().print_help()


if __name__ == "__main__":
    main()
