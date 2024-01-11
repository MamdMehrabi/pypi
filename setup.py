from setuptools import setup, find_packages

setup(
    name = 'name_module',
    version = 'Version Module',
    author= 'Developers',
    author_email = 'Develop gmail',
    description = '',
    keywords = ['کلمات کلیدی مربوط به لایب'],
    long_description = open("README.md", encoding="utf-8").read(),
    python_requires="~=3.6",
    long_description_content_type = 'text/markdown',
    url = 'url/repo',
    packages = find_packages(),
    install_requires = [],
    classifiers = [
    	"Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
    ]
)
