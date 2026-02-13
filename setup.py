from setuptools import setup

setup(
    name="ajju",
    version="3.6.0",
    py_modules=["ajju_do"],
    install_requires=[
        "yt-dlp",
        "rich"
    ],
    entry_points={
        "console_scripts": [
            "ajju=ajju_do:main"
        ],
    },
)
