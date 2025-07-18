from setuptools import setup, find_packages
import os

# Read the contents of your README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read requirements from requirements.txt
def load_requirements():
    with open('requirements.txt') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="neuro-lingo",
    version="0.1.0",
    author="BasiliskBlack",
    author_email="your.email@example.com",  # Update this with your email
    description="A neural-symbolic framework for glyph generation and understanding",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BasiliskBlack/neuro-lingo",
    packages=find_packages(include=['neurolingo*']),
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Multimedia :: Graphics",
    ],
    python_requires='>=3.8',
    install_requires=load_requirements(),
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=3.0.0',
            'black>=22.0.0',
            'isort>=5.10.0',
            'flake8>=4.0.0',
            'mypy>=0.910',
        ],
    },
    entry_points={
        'console_scripts': [
            'neurolingo=neurolingo_demo:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/BasiliskBlack/neuro-lingo/issues',
        'Source': 'https://github.com/BasiliskBlack/neuro-lingo',
    },
)
