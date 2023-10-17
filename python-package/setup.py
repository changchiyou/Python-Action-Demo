from setuptools import find_packages, setup

tests_require = [
    "freezegun",
    "pylint",
    "mypy",
    "pytest",
    "pytest-xdist",
    "pytest-console-scripts",
    "pytest-loguru",
]

setup(
    name="ptest",
    version="0.0.0",
    author="Chris",
    url="https://github.com/changchiyou/Github-Action-Test",
    extras_require={"test": tests_require},
    description="for testing github action",
    packages=find_packages(),
)
