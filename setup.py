import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="foobartory",
    version="0.1",
    author="Francesco Perna",
    description="Little foobartory game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.digeiz.com/pleiades/livedigeiz",
    python_requires=">=3.8",
    package_dir={"foobartory": "src"},
    packages=setuptools.find_packages(exclude=["tests"]),
    install_requires=requirements,
)
