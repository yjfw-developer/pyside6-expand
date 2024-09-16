import os

from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as readme:
    README = readme.read()
setup(
    name="pyside6-expand",
    version="1.0.4",
    author="yjfw",
    author_email="yjfw_developer@163.com",
    description="A expand about pyside6",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/yjfw-developer/pyside6-expand.git",
    packages=find_packages(),
    install_requires=[
        'PySide6'
    ],
    python_requires='>=3.6',
    license='Apache'
)
