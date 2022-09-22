import pytest
from starlette.testclient import TestClient

from main import app

# fixture example
@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    
    return client
