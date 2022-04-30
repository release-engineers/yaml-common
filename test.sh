#!/usr/bin/env bash

mkdir -p test
rm -f test/*.yaml
cp examples/sample-common.yaml test/sample-common.yaml
cp examples/sample-merged-1.yaml test/sample-merged-1.yaml
cp examples/sample-merged-2.yaml test/sample-merged-2.yaml

source .venv/Scripts/activate
./main.py test/sample-common.yaml test/sample-merged-1.yaml test/sample-merged-2.yaml
