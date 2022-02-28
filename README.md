Copyright (c) 2021, Chris MarSil

# cms-python-jenkins

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org)

Projeto FastAPI para testes

## Packages Python usados

- [`pytest`](https://pypi.org/project/pytest/)
- [`pytest-cov`](https://pypi.org/project/pytest-cov/)


## Template workflow file

```yaml
# **************************************************************************************************************** #
# This workflow will install Python dependencies, and run `pytest --cov` on all files recursively from the `pytest-root-dir`
# The workflow is also configured to exit with error if minimum individual file or total pytest coverage minimum not met
# If the workflow exits with error, an informative issue is created for the repo alerting the user
# If the workflow succeeds, a commit message is generated with the `pytest --cov` markdown table
# **************************************************************************************************************** #

name: pytester-cov workflow

on: [push, pull_request]

jobs:
  build:

    runs-on: ubuntu-latest
    env:
      COVERAGE_SINGLE: 60
      COVERAGE_TOTAL: 60

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.9
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
```

## Site CMS

[TamoNaBolsa](https://www.tamonabolsa.com.br/)

