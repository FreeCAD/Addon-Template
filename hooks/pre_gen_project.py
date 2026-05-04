import re
import sys

# validate module name
MODULE_REGEX = r'^[a-zA-Z][_a-zA-Z0-9]+$'
module_name = '{{ cookiecutter.addon_module_name }}'

if not re.match(MODULE_REGEX, module_name):
    print(f'ERROR: {module_name} is not a valid public Python module name!')
    sys.exit(1)


# looooo: it should be possible to name a workbench: freecad.my_workbench, so skip this
# validate project name
# PROJECT_NAME_REGEX = r'^[a-zA-Z]+([A-Z][a-z]+)+$'
# project_name = '{{ cookiecutter.project_slug }}'

# if not re.match(PROJECT_NAME_REGEX, project_name):
#     print(f'ERROR: {project_name} is not a valid camel case project name!')
#     sys.exit(1)