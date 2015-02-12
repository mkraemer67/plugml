# coding=utf8

from setuptools import setup

setup(
    name="plugml",
    version="0.2.3",
    description="easy-to-use and highly modular machine learning framework",
    long_description="easy-to-use and highly modular machine learning framework based on scikit-learn with postgresql data bindings",
    url="https://github.com/mkraemer67/plugml",
    author="Martin Krämer",
    author_email="mkraemer.de@gmail.com",
    license="Apache",
    packages=["plugml"],
    install_requires=[
        "psycopg2>=2.5.0",
    ],
    include_package_data=True,
    zip_safe=False
)
