import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ContrOps",
    version="0.0.1",
    author="Pratham Gandhi",
    author_email="prathamgandhi.school@gmail.com",
    description="Lightweight Python package for converting Signal Temporal Logic into contracts for design-by-contract system design and doing operations on the contracts.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prathgan/ContrOps",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
