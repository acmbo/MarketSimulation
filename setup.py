import setuptools
from setuptools.command.install import install as _install


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MarketSimulation", # Replace with your own username
    version="0.1",
    author="Stephan Wegewitz",
    author_email="sWegewitz@outlook.de",
    description="Package for a simple Simulation of a Marketplace",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    cmdclass={'install': _install},
    install_requires=["pandas","numpy", "matplotlib"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
