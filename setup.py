from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

# requirements = ["smtplib>=0.1"]

setup(
    name="utilities",
    version="0.0.1",
    author="b-diggity",
    description="Utilities to include in Python scripts",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/b-diggity/utilities",
    packages=find_packages(),
    # install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT",
    ],
)
