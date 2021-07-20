from setuptools import setup

setup(
    name="beacon_network",
    version="0.2.dev",
    description="Beacon Network services",
    long_description_content_type="text/markdown",
    project_urls={
        "Source": "https://github.com/CSCfi/beacon-network",
    },
    author="CSC - IT Center for Science",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",
    ],
    packages=[
        "aggregator",
        "aggregator/config",
        "aggregator/endpoints",
        "aggregator/utils",
        "registry",
        "registry/config",
        "registry/endpoints",
        "registry/schemas",
        "registry/utils",
    ],
    package_data={"": ["*.json", "*.ini"]},
    install_requires=[
        "asyncio==3.4.3",
        "aiohttp==3.7.4.post0",
        "aiohttp-cors==0.7.0",
        "aiocache==0.11.1",
        "aiomcache==0.6.0",
        "ujson==4.0.2",
        "uvloop==0.14.0; python_version < '3.7'",
        "uvloop==0.15.3; python_version >= '3.7'",
        "asyncpg==0.23.0",
        "jsonschema==3.2.0",
        "gunicorn==20.1.0",
    ],
    extras_require={
        "test": [
            "coverage==5.5",
            "pytest<6.3",
            "pytest-cov==2.12.1",
            "coveralls==3.1.0",
            "testfixtures==6.18.0",
            "tox==3.24.0",
            "flake8==3.9.2",
            "flake8-docstrings==1.6.0",
            "asynctest==0.13.0",
            "aioresponses==0.7.2",
            "black==21.7b0",
        ],
        "docs": ["sphinx >= 1.4", "sphinx_rtd_theme==0.5.2"],
    },
    entry_points={
        "console_scripts": ["beacon_registry=registry.registry:main", "beacon_aggregator=aggregator.aggregator:main"],
    },
)
