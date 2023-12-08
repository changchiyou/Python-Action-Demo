"""setup ptest."""
from setuptools import find_packages, setup

tests_require = [
    "freezegun",
    "pylint",
    "mypy",
    "pytest",
    "pytest-xdist",
    "pytest-console-scripts",
    "pytest-loguru",
    "types-pytz",
    "pytest-html",
    "pytest-flask",
    "pytest-selenium>=4.0.2",
    "pytest-cov",
    "py",
]

setup(
    name="ptest",
    version="0.0.1",
    author="Chris",
    url="https://github.com/changchiyou/Github-Action-Test",
    extras_require={"test": tests_require},
    description="for testing github action",
    packages=["ptest"],
)
