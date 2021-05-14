import setuptools
from pathlib import Path

VERSION = "0.0.3"

setuptools.setup(
    name="buzzsprout-manager",
    version=VERSION,
    description="A python wrapper for the Buzzsprout API",
    long_description=Path("README.md").read_text(),
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    url="https://github.com/deancolten/buzzsprout-manager",
    author="Colten Dean",
    author_email="coltenrdean@gmail.com",
    install_requires=[
        "requests-toolbelt"
    ]
)
