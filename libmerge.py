from deepdiff import DeepDiff


def get_values(dicts, key):
    values = []
    for obj in dicts:
        values.append(obj[key])
    return values


def merge_delete_common(common, common_key, merged):
    """
    Removes the common part from the merged dictionaries.

    :param common: Dictionary with common values
    :param common_key: Key referencing an entry in common to be merged
    :param merged: Dictionaries from which to remove common values
    """
    common_value = common[common_key]
    for obj in merged:
        if common_key in obj:
            obj_value = obj[common_key]
            diff = DeepDiff(common_value, obj_value)
            if not diff:
                del obj[common_key]
                continue
            if not isinstance(common_value, dict):
                exit(10)
            for key in common_value:
                merge_delete_common(common_value, key, [obj_value])


def merge_entry(common, merged, target, common_key):
    """
    Merge dictionaries by moving all equal common values into the target directory and out of the merged directories.
    :param common: Dictionary with common values
    :param common_key: Key referencing an entry in common to be merged
    :param merged: Dictionaries from which to remove common values
    :param target: Dictionary to which to move common values
    """
    if not isinstance(common, dict) or not isinstance(target, dict):
        return

    # common entry which did not yet exist in target
    if common_key not in target:
        target[common_key] = common[common_key]
        merge_delete_common(common, common_key, merged)
        return

    common_value = common[common_key]
    target_value = target[common_key]

    # common entry matches target already
    diff = DeepDiff(common_value, target_value)
    if not diff:
        return

    merged_values = get_values(merged, common_key)
    merge(common_value, merged_values, target_value)


def merge(common, merged, target):
    """
    Merge dictionaries by moving all equal common values into the target directory and out of the merged directories.
    :param common: Dictionary with common values
    :param merged: Dictionaries from which to remove common values
    :param target: Dictionary to which to move common values
    """
    if not isinstance(common, dict) or not isinstance(target, dict):
        return
    for key in common:
        merge_entry(common, merged, target, key)
