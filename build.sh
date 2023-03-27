#!/bin/bash
rm -rf ./build
rm -rf ./dist
rm -rf *.egg-info
python setup.py bdist_wheel
