from setuptools import setup

APP = ["interface.py"]
DATA_FILES = []
OPTIONS = {
    "argv_emulation": True,
    "packages": ["PyQt5"],
    "iconfile": "ClipLLM.icns",
    "plist": {
        "CFBundleName": "ClipLLM",
        "CFBundleDisplayName": "ClipLLM",
        "CFBundleGetInfoString": "Making ClipLLM",
        "CFBundleIdentifier": "com.yourcompany.ClipLLM",
        "CFBundleVersion": "0.1.0",
        "CFBundleShortVersionString": "0.1.0",
        "NSHumanReadableCopyright": "Copyright © 2023, Your Company, All Rights Reserved",
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
