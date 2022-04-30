#!/usr/bin/env bash

mkdir -p test
rm -f test/*.yaml
cp examples/common.yaml test/common.yaml
cp examples/merged-1.yaml test/merged-1.yaml
cp examples/merged-2.yaml test/merged-2.yaml

source .venv/Scripts/activate
./main.py test/common.yaml test/merged-1.yaml test/merged-2.yaml
