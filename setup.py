#!/usr/bin/env python3

# read the contents of your README file
from os import path

from setuptools import setup

# https://packaging.python.org/guides/making-a-pypi-friendly-readme/
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    # https://packaging.python.org/tutorials/packaging-projects/
    name="helloworld",
    version="0.0.1",
    description="An Hello World!",
    author="Mattia Sappa",
    author_email="m.sappa@reply.com",
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=["helloworld"],
    package_dir={"": "src"},
    # packages=setup().find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        # https://choosealicense.com/
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',

)

# Commands
# python3 setup.py sdist bdist_wheel
# twine check dist/*
# pip install -e .


# Links:
# https://www.youtube.com/watch?v=GIF3LaRqgXo
