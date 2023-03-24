#!/bin/bash
set -e # Exit on failure

# In project root
black --check ./llm
flake8 ./llm
pylint ./llm

# Check cyclomatic complexity
radon cc ./llm