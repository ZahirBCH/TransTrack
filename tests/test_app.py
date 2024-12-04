from modules.trip_management import create_trip
from app import app
import pytest

def test_create_trip():
    data = {
        "trip_date": "2024-12-15",
        "driver": "Ahmed",
        "vehicle": "Truck 1"
    }
    response = create_trip(data)
    assert response["message"] == "Trip created successfully"

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to TransTrack API!" in response.data

def test_create_trip_api(client):
    response = client.post('/create_trip', json={
        "trip_date": "2024-12-15",
        "driver": "Ahmed",
        "vehicle": "Truck 1"
    })
    assert response.status_code == 200
    assert b"Trip created successfully" in response.data