#! /usr/bin/env/python3
#@author -> GEM-404 | EPHANTUS MACHARIA

"""
This module is like the terminal ls command, but for
python3 modules and classes... Whenever I wanna see what
a certain module has, or what to use in it, I will be using
this pyls command to see how it contains.
"""

# import argparse
import importlib
import sys


def get_dirs(package) -> list:
    package = importlib.import_module(package)

    dir_list = dir(package)

    filterd_dirs: list = [directory for directory in dir_list
                      if not directory.startswith('__')]

    return filterd_dirs


def get_dir_starters(args: list, char: str) -> list:

    return [directory for directory in args if directory.startswith(char)]


# check whether the second argument given is a single letter
def check_sec_args(args: list):
    char = sys.argv[2]

    if len(char) == 1 and char.isalpha:
        return get_dir_starters(args=args, char=char)


def check_present_args(package: str, sub_package: str) -> str:
    """Checks whether a sub_module is present in a module"""

    pack_list: list = get_dirs(package)
    checker = sub_package in pack_list

    if checker:
        return f"{sub_package} in {package}"
    return f"{checker}... {sub_package} not present in {package}"


def main():
    package = sys.argv[1]
    print(get_dirs(package))


if __name__ == '__main__':
    main()
