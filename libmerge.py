from deepdiff import DeepDiff


def merge_delete_common(common, common_key, obj):
    """
    Removes common values from objs.

    :param common: Dictionary of values shared by all objs
    :param common_key: Key referencing an entry within common
    :param obj: Dictionaries from which to remove common values
    """
    common_value = common[common_key]
    if common_key in obj:
        obj_value = obj[common_key]
        diff = DeepDiff(common_value, obj_value)
        if not diff:
            del obj[common_key]
            return
        for key in common_value:
            merge_delete_common(common_value, key, obj_value)


def merge_entry(common, objs, target, common_key):
    """
    Moves common values into target and out of objs for a given key.

    :param common: Dictionary of values shared by all objs
    :param common_key: Key referencing an entry within common
    :param objs: Dictionaries from which to remove common values
    :param target: Dictionary in which to move common values
    """
    if not isinstance(common, dict) or not isinstance(target, dict):
        return

    # common entry which did not yet exist in target
    if common_key not in target:
        target[common_key] = common[common_key]
        for obj in objs:
            merge_delete_common(common, common_key, obj)
        return

    common_value = common[common_key]
    target_value = target[common_key]

    # common entry matches target already
    diff = DeepDiff(common_value, target_value)
    if not diff:
        return

    # common entry has different structure in target
    merge(common_value, [obj[common_key] for obj in objs], target_value)


def merge(common, objs, target):
    """
    Moves common values into target and out of objs.

    :param common: Dictionary of values shared by all objs
    :param objs: Dictionaries from which to remove common values
    :param target: Dictionary in which to move common values
    """
    if not isinstance(common, dict) or not isinstance(target, dict):
        return
    for key in common:
        merge_entry(common, objs, target, key)
