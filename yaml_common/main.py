#!/usr/bin/env python

import ruamel.yaml
from yaml_common.libcommon import common
from yaml_common.libmerge import merge


class CLI(object):
    # noinspection PyMethodMayBeStatic
    def merge(self, *file_names):
        yaml = ruamel.yaml.YAML()
        yaml.preserve_quotes = True
        file_data = []

        for filename in file_names:
            with open(filename, 'r') as f:
                file_data.append(yaml.load(f) or {})

        data_original_common = file_data[0]
        data_others = file_data[1:]

        data_common_of_others = common(data_others)
        merge(data_common_of_others, data_others, data_original_common)

        for i, filename in enumerate(file_names):
            with open(filename, 'w') as f:
                yaml.dump(file_data[i], f)
