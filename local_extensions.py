from cookiecutter.utils import simple_filter

import re


@simple_filter
def svg_filename(v: str | None) -> str:
    if v is None:
        return "addon"
    if v.lower().endswith(".svg"):
        v = v[:-4]
    return re.sub(r'\W+', '-', v)


@simple_filter
def proj_dir(v: str | None) -> str:
    if v is None:
        return "MyAddon"
    return re.sub(r"\W+", "_", v)


@simple_filter
def module_name(v: str | None) -> str:
    if v is None:
        return "MyAddon"
    return re.sub(r"\W+", "_", v)
