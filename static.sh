#!/bin/bash
set -e # Exit on failure

# In project root
black --check ./llm
flake8 ./llm
pylint ./llm --ignore=migrations

# Check cyclomatic complexity
radon cc ./llm