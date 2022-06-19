#!/usr/bin/env python3

from os import system as sh
from os import mkdir
from shutil import rmtree
from os import chdir
from sys import argv


MAIN: str = "uxptl.py"

PYFLAGS: str = """ \
    -OO \
"""

CFLAGS: str = """ \
    --warn-implicit-exceptions \
    --warn-unusual-code \
    --follow-imports \
    --python-flag=-OO \
    --disable-ccache \
    --lto=yes \
"""

BINDIR: str = "/usr/local/bin"


BUILD: str = f"python {PYFLAGS} -m nuitka {CFLAGS} -o uxptl ../{MAIN}"


if len(argv) == 1:
    print("incorrect flags")

elif argv[1] == "install":
    try:
        mkdir("build/")

    except FileExistsError:
        rmtree("build/")
        mkdir("build/")
        chdir("build/")

    sh(BUILD)
    sh(f"sudo mv uxptl {BINDIR}")

elif argv[1] == "build":
    try:
        mkdir("build/")

    except FileExistsError:
        rmtree("build/")
        mkdir("build/")
        chdir("build/")

    sh(BUILD)

else:
    print("incorrect flags")