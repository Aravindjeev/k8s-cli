from setuptools import setup, find_packages

setup(
    name="k8s-cli",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "rich",
        "pyyaml"
    ],
    entry_points={
        "console_scripts": [
            "k8s-cli = bin.k8s_cli:main",
        ],
    },
)
