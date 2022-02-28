Copyright (c) 2021, Chris MarSil

# cms-python-jenkins

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org)

Projeto FastAPI para testes

## Packages Python usados

- [`fastapi`](https://pypi.org/project/fastapi/)
- [`fastapi-login`](https://pypi.org/project/fastapi-login/)
- [`uvicorn`](https://pypi.org/project/uvicorn/)
- [`pytest`](https://pypi.org/project/pytest/)
- [`pytest-cov`](https://pypi.org/project/pytest-cov/)

## Exemplo

* Arquivo `main.py`:

```Python
# **************************************************************************************************************** #
# Código
# **************************************************************************************************************** #

from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
```

## Site CMS

[TamoNaBolsa](https://www.tamonabolsa.com.br/)

