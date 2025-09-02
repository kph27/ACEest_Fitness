from flask import Flask, request, jsonify

app = Flask(__name__)

workouts = []

@app.route('/')
def home():
    return "Welcome to ACEest Fitness and Gym API!"

@app.route('/add_workout', methods=['POST'])
def add_workout():
    data = request.json
    if not data or 'workout' not in data or 'duration' not in data:
        return jsonify({'error': 'Workout and duration required'}), 400
    workouts.append({'workout': data['workout'], 'duration': data['duration']})
    return jsonify({'message': f"{data['workout']} added successfully!"}), 201

@app.route('/workouts', methods=['GET'])
def get_workouts():
    return jsonify({'workouts': workouts}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

