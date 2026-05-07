#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RegexForge - Lightweight Regular Expression Testing, Debugging & Visualization CLI Tool
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="regexforge",
    version="1.0.0",
    author="gitstq",
    author_email="",
    description="Lightweight Regular Expression Testing, Debugging & Visualization CLI Tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gitstq/RegexForge",
    py_modules=["regexforge"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Regular Expressions",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "regexforge=regexforge:main",
        ],
    },
    keywords="regex regular-expression testing debugging cli tool code-generator pattern-library",
)
