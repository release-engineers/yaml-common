#!/usr/bin/env python

import sys
import ruamel.yaml
from deepdiff import DeepDiff

yaml = ruamel.yaml.YAML()
yaml.preserve_quotes = True

datas = []

for filename in sys.argv[1:]:
    with open(filename, 'r') as f:
        data = yaml.load(f)
        datas.append(data)

common_data = datas[0]
common_data_filename = sys.argv[1]
specific_datas = datas[1:]
specific_datas_filenames = sys.argv[2:]

# print yamls
print('---')
print('# common data from {}'.format(common_data_filename))
yaml.dump(common_data, sys.stdout)

for data in specific_datas:
    print('---')
    print('# specific data from {}'.format(specific_datas_filenames[specific_datas.index(data)]))
    yaml.dump(data, sys.stdout)
    sys.stdout.write('\n')

# print(DeepDiff(specific_datas[0], specific_datas[1]))
