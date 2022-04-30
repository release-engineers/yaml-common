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
        data = yaml.load(f) or {}
        datas.append(data)

source_common = datas[0]
source_common_filename = sys.argv[1]
merged_datas = datas[1:]
merged_datas_filenames = sys.argv[2:]

common_of_merged = common(merged_datas)
merge(common_of_merged, merged_datas, source_common)
yaml.dump(source_common, sys.stdout)
