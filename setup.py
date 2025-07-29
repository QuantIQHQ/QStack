from setuptools import setup, find_packages

setup(
    name="qstack",
    version="0.1.0",
    description="Modern fullstack project generator by QuantIQ - for vibecoders",
    author="QuantIQ Devs",
    packages=find_packages(),
    install_requires=[
        "click>=8.0.0",
        "jinja2>=3.0.0",
        "colorama>=0.4.4",
        "pyyaml>=6.0",
    ],
    entry_points={
        "console_scripts": [
            "qstack=qstack.cli:main",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)