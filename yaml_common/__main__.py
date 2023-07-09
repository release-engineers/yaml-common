import fire
from yaml_common.main import CLI


def main():
    fire.Fire(component=CLI, name="yaml-common")


if __name__ == "__main__":
    main()
