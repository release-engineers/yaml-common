#!/usr/bin/env python

import sys
import ruamel.yaml

yaml = ruamel.yaml.YAML()
yaml.preserve_quotes = True

data_by_filename = {}

for filename in sys.argv[1:]:
    with open(filename, 'r') as f:
        data = yaml.load(f)
        data_by_filename[filename] = data

for filename, data in data_by_filename.items():
    print('---')
    print('# {}'.format(filename))
    print('')
    yaml.dump(data, sys.stdout)
