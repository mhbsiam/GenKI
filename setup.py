import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
DESCRIPTION = "GenKI"
PACKAGES = find_packages(exclude=("tests*",))
exec(open('GenKI/version.py').read())

INSTALL_REQUIRES = [
        "anndata>=0.10",
        "matplotlib>=3.8",
        "numpy>=1.24,<2.4",
        "pandas>=2.0",
        "ray>=2.30",
        "scanpy>=1.12",
        "scipy>=1.12",
        "statsmodels>=0.14",
        "scikit-learn>=1.4",
        "tqdm>=4.66",
    ]

setup(
    name="GenKI",
    version=__version__,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/yjgeno/GenKI",
    author="Yongjian Yang, TAMU",
    author_email="yjyang027@tamu.edu",
    license="MIT",
    keywords=[
        "neural network",
        "graph neural network",
        "variational graph neural network",
        "computational-biology",
        "single-cell",
        "gene knock-out",
        "gene regulatroy network",
    ],
    classifiers=[
    "License :: OSI Approved :: MIT License",
    "Intended Audience :: Science/Research",
    "Topic :: Scientific/Engineering :: Bio-Informatics",
    "Programming Language :: Python :: 3",
    ],
    packages=PACKAGES,
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
)