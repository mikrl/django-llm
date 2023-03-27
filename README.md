[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3112/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Django LLM
An app for Django to aid development of large language model (LLM) workflows.

Have you ever wanted to store ChatGPT queries in your database? Now you can.

Powered by [langchain](https://github.com/hwchase17/langchain)


* [Wiki](https://github.com/mikrl/django-llm/wiki)
* [Sample Project](https://github.com/mikrl/django-llm-sample)

# Information
Configure your LLM workflow from Django.

Build a business layer for your LLM application.

## Install latest binary
```bash
pip install django-llm
```

## Build and install from source
```bash
./build.sh
pip install dist/*.whl
```

# Tests
```bash
pip install -r static.txt
./static.sh
pytest tests/
```

# Features
* Model to configure and execute ChatGPT query
* Model to hold prompt and determine prompt variables
* Model to store API keys for various services
