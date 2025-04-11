#!/usr/bin/env python3
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="context-guide",
    version="0.1.0",
    author="Diego Nogueira",
    author_email="devnogueiradiego@gmail.com",
    description="Ferramenta de contexto para IDEs assistidas por IA",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DiegoNogueiraDev/context-guide",
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
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ],
        "mcp": [
            "fastapi>=0.104.0",
            "uvicorn>=0.24.0",
            "pydantic>=2.4.0",
            "requests>=2.31.0",
        ],
    },
) 