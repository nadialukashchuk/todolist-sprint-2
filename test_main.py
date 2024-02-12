from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_get_all_tasks():
    response = client.get('/task')
    assert response.status_code == 200