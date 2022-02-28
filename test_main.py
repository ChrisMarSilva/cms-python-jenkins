from typing import Generator
import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture(scope="function")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


client_local = TestClient(app)


def test_read_root():
    response = client_local.get(url="/test")
    body = response.json()
    assert response.status_code == 200
    assert body["message"] == "Hello World"

# pytest
# pytest -v
# pytest -vv
# pytest --cov=test_
