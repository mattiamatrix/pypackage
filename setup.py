from os import path

from setuptools import setup, find_packages

# read the contents of your README file
# https://packaging.python.org/guides/making-a-pypi-friendly-readme/
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    # https://packaging.python.org/tutorials/packaging-projects/
    name="helloworld",
    version="0.1.2",
    description="An Hello World!",
    author="Mattia Sappa",
    author_email="m.sappa@reply.com",
    url="https://github.com/mattiamatrix/pypackage",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",  # https://choosealicense.com/
    ],
    python_requires=">=3.6",
    # install_requires=[],
    # extras_require={},
    tests_require=["pytest"],
)

# Commands
# python3 setup.py develop
# python3 setup.py bdist bdist_wheel
# twine check dist/*
# pip install -e .
# check-manifest --create


# Links:
# https://www.youtube.com/watch?v=GIF3LaRqgXo
# https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/
