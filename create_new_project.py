#!/usr/bin/env python3
import os

from argparse import ArgumentParser
from pathlib import Path

from jinja2 import Template

BACKEND_TOOL_OPTIONS = {
    "httpie": [
        "--pretty=all",
    ],
}


def create_project(project_name: str) -> str:
    project_path = Path.joinpath(Path.cwd(), project_name)
    if not project_path.exists():
        print("")
        os.mkdir(project_name)
    else:
        print(f"Project folder has already been created: {project_path}")

    return project_path


def read_file(file_path: str) -> str:
    return open(file_path, mode="rb").read()

def copy_templates(env_variables: dict, project_path: str):
    local_ain_content = read_file("templates/local.ain.j2")
    local_ain_template = Template(local_ain_content)
    local_ain_template.render(**env_variables)


def create_cli_arguments():
    parser = ArgumentParser()
    parser.add_argument("--project_name", help="The name of the project you want to create")
    parser.add_argument("--dev_port", help="The port used for the dev template", default=8000)
    parser.add_argument("--tool", help="You can choose between: curl, wget, httpie", default="httpie")
    return parser


if __name__ == "__main__":
    arguments = create_cli_arguments().parse_args()

    project_path = create_project(project_name=arguments.project_name)

    environment_varables = {
        "backend_tool": arguments.tool,
        "http_port": arguments.dev_port,
    }
