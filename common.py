from collections import OrderedDict
from deepdiff import DeepDiff
import copy


def get_keys(dicts):
    """
    Extract all keys from all given dictionaries, attempting to preserving order.
    :param dicts:
    :return:
    """
    keys = []
    for obj in dicts:
        keys.extend(obj.keys())
    return list(OrderedDict.fromkeys(keys).keys())


def get_values(dicts, key):
    values = []
    for obj in dicts:
        values.append(obj[key])
    return values


def all_equal_length(candidates):
    base = len(candidates[0])
    for candidate in candidates:
        if len(candidate) != base:
            return False
    return True


def all_are_lists(candidates):
    for candidate in candidates:
        if not isinstance(candidate, list):
            return False
    return True


def all_are_dicts(candidates):
    for candidate in candidates:
        if not isinstance(candidate, dict):
            return False
    return True


def all_contain_key(candidates, key):
    for candidate in candidates:
        if key not in candidate:
            return False
    return True


def all_equal(merged_objs):
    """
    Check if all given objects' values are equal to each other.
    :param merged_objs:
    :return: boolean
    """
    base = merged_objs[0]
    for merged_obj in merged_objs[1:]:
        diff = DeepDiff(base, merged_obj)
        if diff:
            return False
    return True


def common_dict(dicts):
    """
    Extract common object from all given dictionaries.
    :param dicts:
    :return:
    """
    dict_common = {}
    for key in get_keys(dicts):
        if not all_contain_key(dicts, key):
            continue
        values = get_values(dicts, key)
        if all_equal(values):
            dict_common[key] = copy.deepcopy(values[0])
        else:
            value_common = common(values)
            if value_common:
                dict_common[key] = copy.deepcopy(value_common)
    return dict_common


def common(values):
    """
    Extract common dictionary entries from all given values.
    :param values:
    :return:
    """
    if all_are_dicts(values):
        return common_dict(values)
    if all_equal(values):
        return values[0]
    return None
