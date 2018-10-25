#!/usr/bin/env python3
from setuptools import setup, find_packages


setup(
    name="",
    version="0.01",
    packages=find_packages(),
    install_requires=[
        "fitbit"
    ],
    dependency_links=[
    ],
    extras_require={
        "tests": [
            "flake8",
            "autopep8",
        ]
    }
)
