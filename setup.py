"""setup ptest."""
from setuptools import find_packages, setup


def read_requirements(file_path: str) -> list[str]:
    """Read requirements from a file."""
    with open(file_path, "r", encoding="utf-8") as _file:
        return [line.strip() for line in _file.readlines()]


setup(
    name="ptest",
    version="0.0.1",
    author="Chris",
    url="https://github.com/changchiyou/Github-Action-Test",
    install_require=read_requirements(file_path="./requirements.txt"),
    extras_require={"test": read_requirements(file_path="./requirements-dev.txt")},
    description="for testing github action",
    packages=find_packages(where=".", exclude=["tests.*", "tests"]),
)
