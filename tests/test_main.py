import os

from yaml_common.main import CLI


def test_merge(tmp_path):
    tmp_path = tmp_path / "merge"
    tmp_path.mkdir()
    source_dir = os.path.join(os.path.dirname(__file__), "data")

    def copied(name):
        source_path = str(os.path.join(source_dir, name))
        target_path = str(tmp_path / name)
        with open(source_path, "r") as source, open(target_path, "w") as target:
            target.write(source.read())
        return target_path

    path_copy_common = copied("common.yaml")
    path_copy_1 = copied("1.yaml")
    path_copy_2 = copied("2.yaml")

    cli = CLI()
    cli.merge(path_copy_common, path_copy_1, path_copy_2)

    path_expected_common = str(os.path.join(source_dir, "common_expected.yaml"))
    with open(path_expected_common, "r") as expected, open(path_copy_common, "r") as actual:
        assert expected.read() == actual.read()

    path_expected_1 = str(os.path.join(source_dir, "1_expected.yaml"))
    with open(path_expected_1, "r") as expected, open(path_copy_1, "r") as actual:
        assert expected.read() == actual.read()

    path_expected_2 = str(os.path.join(source_dir, "2_expected.yaml"))
    with open(path_expected_2, "r") as expected, open(path_copy_2, "r") as actual:
        assert expected.read() == actual.read()
