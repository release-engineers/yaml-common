<!-- README.md is auto-generated from README.md.template -->

# release-engineers/yaml-common

[![Status: Production ready](https://img.shields.io/badge/status-production_ready-green)](https://release-engineers.com/open-source-badges/)
[![PyPI version](https://badge.fury.io/py/re-yaml-common.svg)](https://badge.fury.io/py/re-yaml-common)

Extracts and merges common parts of YAML from one set of files into a common file.
Note that this project attempts to preserve comments and order of properties in your YAML files, but can not preserve formatting.

## Setup

```bash
pip install re-yaml-common
```

## Usage

`yaml-common merge <common file> <file 1> <file 2> ...`

An example below for `yaml-common merge tests/data/common.yaml tests/data/1.yaml tests/data/2.yaml`.

#### Input

Content of `common.yaml`:
```yml common
example-exists:
  str-1: This property already exists in common.yaml
  str-2: This property exists in all files

```

Content of `1.yaml`:
```yml
example-common:
  # common comment
  depth:
    more-depth:
      array:
      - yes
      - for sure
      str: common string
    int: 123
    float: 1.23
  bool: true
  null:
example-specific:
  depth:
    more-depth:
      # specific comment to 1.yaml
      str-specific: 1.yaml
example-exists:
  str-2: This property exists in all files, and is overridden by 1.yaml
example-mixed:
  array-common:
  - yes
  - for sure again
  array-specific:
  - no
  - because this is specific to 1.yaml
  str-common: common string
  str-specific: 1.yaml
  sre-common-multiline: |
    -----BEGIN PUBLIC KEY-----
    01234567890
    -----END PUBLIC KEY-----
  unique-to-1: this property is unique to 1.yaml

```

Content of `2.yaml`:
```yml
example-common:
  # common comment
  depth:
    more-depth:
      array:
      - yes
      - for sure
      str: common string
    int: 123
    float: 1.23
  bool: true
  null:
example-specific:
  depth:
    more-depth:
      # specific comment to 2.yaml
      str-specific: 2.yaml
example-exists:
  str-2: This property exists in all files, and is overridden by 2.yaml
example-mixed:
  array-common:
  - yes
  - for sure again
  array-specific:
  - no
  - because this is specific to 2.yaml
  str-common: common string
  str-specific: 2.yaml
  sre-common-multiline: |
    -----BEGIN PUBLIC KEY-----
    01234567890
    -----END PUBLIC KEY-----

```

#### Output

After running the above example, the content of the files will have changed to:

Expected content of `common.yaml`:
```yml
example-exists:
  str-1: This property already exists in common.yaml
  str-2: This property exists in all files
example-common:
  # common comment
  depth:
    more-depth:
      array:
      - yes
      - for sure
      str: common string
    int: 123
    float: 1.23
  bool: true
  null:
example-mixed:
  array-common:
  - yes
  - for sure again
  str-common: common string
  sre-common-multiline: |
    -----BEGIN PUBLIC KEY-----
    01234567890
    -----END PUBLIC KEY-----

```

Expected content of `1.yaml`:
```yml
example-specific:
  depth:
    more-depth:
      # specific comment to 1.yaml
      str-specific: 1.yaml
example-exists:
  str-2: This property exists in all files, and is overridden by 1.yaml
example-mixed:
  array-specific:
  - no
  - because this is specific to 1.yaml
  str-specific: 1.yaml
  unique-to-1: this property is unique to 1.yaml

```

Expected content of `2.yaml`:
```yml
example-specific:
  depth:
    more-depth:
      # specific comment to 2.yaml
      str-specific: 2.yaml
example-exists:
  str-2: This property exists in all files, and is overridden by 2.yaml
example-mixed:
  array-specific:
  - no
  - because this is specific to 2.yaml
  str-specific: 2.yaml

```

## Contributing

This is a Python Poetry project using [Fire](https://github.com/google/python-fire).
See [Poetry](https://python-poetry.org/) for more information.

Development requires:

- Bash
- [Docker](https://www.docker.com/)
- [Python](https://www.python.org/)
- [Poetry](https://python-poetry.org/)

## Links

This project was created using [template-poetry](https://github.com/release-engineers/template-poetry).
