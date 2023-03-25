[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3112/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Django LLM
An app for Django to aid development of LLM workflows

# Information
Some models for coordinating LLM tasks. Provides a Django wrapper for langchain and openai.

## Installation
`pip install -r requirements.txt` 

## Installation from binary
`python setup.py bdist_whl && pip install dist/*.whl`

# Tests
`pip install -r static.txt`

`./static.sh`

`pytest tests/`

# Features
Model to store API key in database
Model to hold prompt
Model to make a ChatGPT query (under development)
 
#TODO Endpoints for prompts (CRUD)
#TODO Mopdels and endpoints for memory
#TODO Endpoint for OpenAI queries
