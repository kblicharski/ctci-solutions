#!/bin/bash
# Basic cleanup script to clean up my solutions.

# Fix pep8 violations
autopep8 . --recursive --in-place --pep8-passes 2000 --verbose

# Reorder imports
isort -rc .

# Verify that there are no more violations
output=$(pycodestyle --statistics --max-line-length=100 .)
