#!/bin/bash
set -e

# In project root
black --check ./llm
pylint ./llm

# Check cyclomatic complexity
radon cc ./llm