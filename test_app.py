from fastapi.testclient import TestClient
from app.app import app

client=TestClient(app)

def test_app():
    response=client.get('/')
    assert response.status_code==200
    assert response.json()== {'message':'You are in home page'}