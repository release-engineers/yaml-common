#!/usr/bin/env bash

mkdir -p test
cp examples/common.yaml test/common.yaml
cp examples/1.yaml test/1.yaml
cp examples/2.yaml test/2.yaml

source venv/bin/activate || source venv/Scripts/activate
./main.py test/common.yaml test/1.yaml test/2.yaml
deactivate
