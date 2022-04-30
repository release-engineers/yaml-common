<!-- README.md is auto-generated from README.md.template -->

# [EffortGames/yaml-common](https://github.com/EffortGames)

Extracts and merges common parts of YAML from one set of files into a common file.
Note that this project attempts to preserve comments and order of properties in your YAML files, but can not preserve formatting.

## Setup

```bash
#!/usr/bin/env bash

python -m venv venv
source venv/bin/activate || source venv/Scripts/activate
pip install -r requirements.txt

```

## Usage

`main.py <common file> <file 1> <file 2> ...`

See [usage.sh](usage.sh). It demonstrates moving the common parts of "1.yaml" and "2.yaml" into "common.yaml" where it does not already contain its own definition;

```bash
#!/usr/bin/env bash

mkdir -p test
cp examples/common.yaml test/common.yaml
cp examples/1.yaml test/1.yaml
cp examples/2.yaml test/2.yaml

source venv/bin/activate || source venv/Scripts/activate
./main.py test/common.yaml test/1.yaml test/2.yaml
deactivate

```

#### Input

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

Content of `common.yaml`:
```yml common
example-exists:
  str-1: This property already exists in common.yaml
  str-2: This property exists in all files

```

#### Output

After running the above example, the content of the files will have changed to:

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
