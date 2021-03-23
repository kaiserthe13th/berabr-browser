import os, sys, PyQt5
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

options = {
    "build_exe": {
            "zip_include_packages": [
            "PyQt5",
            "shiboken2",
            "encodings",
        ],  # reduce size of packages that are used
        "excludes": [
            "tkinter",
            "unittest",
            "email",
            "http",
            "xml",
            "pydoc",
            "pdb",
        ],  # exclude packages that are not really needed
    }
}

setup (
    name = "Berabr Browser",
    version = "0.0.3",
    description = "A Ligthweight And Fast Browser - Berabr Browser",
    options = options,
    executables = [Executable("main.py", base=base)]
)