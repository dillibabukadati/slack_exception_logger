# Created by @dillibk777 at 15/01/23
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='slack_exception_logger',
    version='0.3',
    author='Dilli Babu Kadati',
    author_email='dillibabukadati777@gmail.com',
    description='A Python library for logging exceptions to a Slack channel',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/dillibk777/slack_exception_logger',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests'
    ],
)
