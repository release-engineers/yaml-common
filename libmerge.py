from deepdiff import DeepDiff


def get_values(dicts, key):
    values = []
    for obj in dicts:
        values.append(obj[key])
    return values


def merge_entry_perform(common, common_key, merged, target):
    """
    Perform the actual merge from common to target and removing entries from merged.

    :param common: Dictionary with common values
    :param common_key: Key referencing an entry in common to be merged
    :param merged: Dictionaries from which to remove common values
    :param target: Dictionary to which to move common values
    """
    target[common_key] = common[common_key]
    for obj in merged:
        if common_key in obj:
            del obj[common_key]


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
        merge_entry_perform(common, common_key, merged, target)
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
