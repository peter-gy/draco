#!/usr/bin/env python

from codecs import open
from os.path import abspath, dirname, join
from subprocess import call
from time import time
from typing import List

from draco1 import __version__
from setuptools import Command, setup

this_dir = abspath(dirname(__file__))
with open(join(this_dir, "README.md"), encoding="utf-8") as file:
    long_description = file.read()


class RunTests(Command):
    """Run all tests."""

    description = "run tests"
    user_options: List[str] = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        print("=> Running Ansunit Tests:")

        errno_ansunit = call(["ansunit", "asp/tests.yaml", "-v"])

        print("=> Running JS Tests:")

        errno_js = call(["yarn", "--cwd", "js", "test"])

        print("\n\n=> Running Python Tests:")
        start = int(round(time() * 1000))

        errno_pytest = call(
            [
                "pytest",
                "tests",
                "--cov=draco",
                "--cov-report=xml",
                "--cov-report=term-missing",
            ]
        )

        end = int(round(time() * 1000))

        print("\n\n RAN IN: {0} sec".format((end - start) / 1000))

        print("\n\n=> Running MyPy:")
        errno_mypy = call(["mypy", "draco", "tests", "--ignore-missing-imports"])

        print("\n\n=> Running Black:")
        errno_mypy = call(["black", "--check", "."])

        print("=> Running Prettier:")

        errno_prettier = call(["yarn", "--cwd", "js", "lint"])

        raise SystemExit(
            errno_ansunit + errno_js + errno_pytest + errno_mypy + errno_prettier
        )


setup(
    name="draco1",
    version=__version__,
    description="Visualization recommendation using constraints",
    long_description=long_description,
    author="Dominik Moritz, Chenglong Wang",
    author_email="domoritz@cs.washington.edu, clwang@cs.washington.edu",
    license="BSD-3",
    url="https://github.com/uwdata/draco",
    packages=["draco1"],
    entry_points={"console_scripts": ["draco1=draco1.cli:main"]},
    install_requires=["clyngor"],
    include_package_data=True,
    extras_require={
        "test": ["coverage", "pytest", "pytest-cov", "black", "ansunit", "mypy"]
    },
    package_data={
        "draco1": [
            "../asp/*.lp",
            "../js/bin/*",
            "../js/build/draco.js*",
            "../LICENSE",
            "../README.md",
        ]
    },
    cmdclass={"test": RunTests},
)
