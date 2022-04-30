#!/usr/bin/env python

import sys
import ruamel.yaml
from libcommon import common
from libmerge import merge

yaml = ruamel.yaml.YAML()
yaml.preserve_quotes = True
datas = []

for filename in sys.argv[1:]:
    with open(filename, 'r') as f:
        datas.append(yaml.load(f) or {})

source_common = datas[0]
merged_datas = datas[1:]

common_of_merged = common(merged_datas)
merge(common_of_merged, merged_datas, source_common)

for i, filename in enumerate(sys.argv[1:]):
    with open(filename, 'w') as f:
        yaml.dump(datas[i], f)
