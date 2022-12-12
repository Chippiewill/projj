#!/usr/bin/python3

from pathlib import Path

developer = Path("~/Developer").expanduser()

to_explore = [developer]
projects = []

MAX_DEPTH = 9

while to_explore:
    cwd = to_explore.pop()

    child_dirs = []
    for child in cwd.iterdir():
        if child.is_dir() and not child.is_symlink():
            if child.name == ".git":
                projects.append(cwd)
                print(cwd)
                break
            child_dirs.append(child)
        if child.name in (".catkin_workspace", ".catkin_tools"):
            projects.append(cwd / "src")
            print(cwd / "src")
            break
    else:
        # Don't recurse too deeply
        if len(cwd.parents) <= MAX_DEPTH:
            to_explore += child_dirs

# for project in projects:
#     print(project)