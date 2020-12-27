#!/bin/bash


SCRIPT=$(readlink $0)
PYTHON_SCRIPT=${SCRIPT%.*}.py

/usr/bin/python3 $PYTHON_SCRIPT $@
