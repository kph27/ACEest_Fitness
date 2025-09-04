import pytest
import app

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_workout_not_string(client):
    # workout is a number, should fail
    response = client.post('/workouts', json={'workout': 300, 'duration': 200})
    assert response.status_code == 400
    assert b"Valid 'workout' (non-empty string) is required" in response.data

def test_duration_not_number(client):
    # duration is a string, should fail
    response = client.post('/workouts', json={'workout': "Benchpress", 'duration': "10m"})
    assert response.status_code == 400
    assert b"'duration' must be a positive integer" in response.data

def test_valid_workout_entry(client):
    # Both inputs are valid, should succeed
    response = client.post('/workouts', json={'workout': "Dumbbell press", 'duration': 20})
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data['workout']['workout'] == "Dumbbell press"
    assert json_data['workout']['duration'] == 20
    assert "added successfully" in json_data['message']
