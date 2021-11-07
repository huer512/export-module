'''
Author: 兄弟们Go
Date: 2021-11-07 16:54:43
LastEditTime: 2021-11-07 16:59:17
LastEditors: 兄弟们Go
Description: 
FilePath: \pymodules\setup.py

'''
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymodules", # Replace with your own username
    version="0.0.1",
    author="xdykj",
    author_email="xdykj@outlook.com",
    description="A package that try to solve the problem of import function",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://multiblock.coding.net/p/yunxunlian/d/pymodules/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
    ],
    python_requires='>=3.6',
)
