from flask import Flask, request, jsonify, abort

app = Flask(__name__)

workouts = []
workout_id_counter = 1

def find_workout(workout_id):
    for workout in workouts:
        if workout['id'] == workout_id:
            return workout
    return None

@app.route('/')
def home():
    return "Welcome to ACEest Fitness and Gym API!"

@app.route('/workouts', methods=['GET'])
def get_workouts():
    """Return a list of all workouts."""
    return jsonify({'workouts': workouts, 'total_workouts': len(workouts)}), 200

@app.route('/workouts/total_duration', methods=['GET'])
def total_duration():
    """Sum total duration of all recorded workouts."""
    total = sum(w['duration'] for w in workouts)
    return jsonify({'total_duration_minutes': total}), 200

@app.route('/workouts/<int:workout_id>', methods=['GET'])
def get_workout(workout_id):
    """Get a single workout by its ID."""
    workout = find_workout(workout_id)
    if workout is None:
        abort(404, description=f"Workout with id {workout_id} not found")
    return jsonify(workout), 200

@app.route('/workouts', methods=['POST'])
def add_workout():
    """
    Add a new workout.
    JSON body expects: {"workout": <string>, "duration": <int>}
    """
    global workout_id_counter
    data = request.json
    if not data:
        abort(400, description="JSON body required")
    workout_name = data.get('workout')
    duration = data.get('duration')

    if not isinstance(workout_name, str) or not workout_name.strip():
        abort(400, description="Valid 'workout' (non-empty string) is required")
    if not isinstance(duration, int) or duration <= 0:
        abort(400, description="'duration' must be a positive integer")

    workout = {
        'id': workout_id_counter,
        'workout': workout_name.strip(),
        'duration': duration
    }
    workouts.append(workout)
    workout_id_counter += 1

    return jsonify({'message': f"Workout '{workout_name}' added successfully!", 'workout': workout}), 201

@app.route('/workouts/<int:workout_id>', methods=['PUT'])
def update_workout(workout_id):
    """
    Update an existing workout by ID.
    JSON body can include 'workout' and/or 'duration'.
    """
    workout = find_workout(workout_id)
    if workout is None:
        abort(404, description=f"Workout with id {workout_id} not found")

    data = request.json
    if not data:
        abort(400, description="JSON body required")

    workout_name = data.get('workout')
    duration = data.get('duration')

    if workout_name is not None:
        if not isinstance(workout_name, str) or not workout_name.strip():
            abort(400, description="If provided, 'workout' must be a non-empty string")
        workout['workout'] = workout_name.strip()

    if duration is not None:
        if not isinstance(duration, int) or duration <= 0:
            abort(400, description="If provided, 'duration' must be a positive integer")
        workout['duration'] = duration

    return jsonify({'message': f"Workout id {workout_id} updated successfully", 'workout': workout}), 200

@app.route('/workouts/<int:workout_id>', methods=['DELETE'])
def delete_workout(workout_id):
    """Delete a workout by its ID."""
    workout = find_workout(workout_id)
    if workout is None:
        abort(404, description=f"Workout with id {workout_id} not found")

    workouts.remove(workout)
    return jsonify({'message': f"Workout id {workout_id} deleted successfully"}), 200

# Error handlers for better JSON response on errors
@app.errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e.description)), 400

@app.errorhandler(404)
def not_found(e):
    return jsonify(error=str(e.description)), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify(error="Internal server error"), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
