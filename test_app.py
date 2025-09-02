import pytest
import app

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_home(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"Welcome to ACEest Fitness and Gym" in rv.data

def test_add_workout(client):
    response = client.post('/add_workout', json={'workout': 'Run', 'duration': 30})
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data['message'] == 'Run added successfully!'

def test_get_workouts(client):
    client.post('/add_workout', json={'workout': 'Run', 'duration': 30})
    response = client.get('/workouts')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data['workouts']) > 0

