#!/usr/bin/env python3
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="context-guide",
    version="0.1.0",
    author="Seu Nome",
    author_email="seu.email@exemplo.com",
    description="Ferramenta de contexto para IDEs assistidas por IA",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seuusuario/context-guide",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        "llama-index>=0.9.0",
        "chromadb>=0.4.18",
        "watchdog>=3.0.0",
        "pyperclip>=1.8.2",
        "python-dotenv>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "context-guide=context_guide.cli:main",
        ],
    },
) 