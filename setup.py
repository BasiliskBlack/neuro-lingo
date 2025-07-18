from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="neuro-lingo",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A neural-symbolic framework for glyph generation and understanding",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/neuro-lingo",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires='>=3.8',
    install_requires=[
        "numpy>=1.21.0",
        "matplotlib>=3.4.0",
        "torch>=1.9.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "isort>=5.10.0",
            "flake8>=4.0.0",
            "mypy>=0.910",
            "pytest-cov>=3.0.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "neurolingo=neurolingo_demo:main",
        ],
    },
)
