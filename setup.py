"""lambdata - a collections of  Data Science helper functions"""

import setuptools

REQUIRED = [
    "numpy",
    "pandas"
]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()


setuptools.setup(
    name="lambdata-joeymckinney",
    version="0.0.1",
    authoer="joeymckinney",
    description='A collection of Data Science help functions',
    long_description=LONG_DESCRIPTION,
    long_description_content='text/markdown',
    url="https://github.com/joeyMckinney/lambdata",
    packages=setuptools.find_packages(),
    python_requires='>=3.8',
    install_requires=REQUIRED,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operation system :: OS Independent',
    ]
)
