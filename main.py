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

data_original_common = datas[0]
data_others = datas[1:]

data_common_of_others = common(data_others)
merge(data_common_of_others, data_others, data_original_common)

for i, filename in enumerate(sys.argv[1:]):
    with open(filename, 'w') as f:
        yaml.dump(datas[i], f)
