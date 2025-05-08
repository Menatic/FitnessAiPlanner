import os
import logging
from flask import Flask, request, jsonify, render_template
from workout_generator import generate_workout_plan
from utils import validate_input

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default-secret-key")

@app.route('/')
def index():
    """Render the home page with the form to test the API."""
    return render_template('index.html')

@app.route('/documentation')
def documentation():
    """Render the API documentation page."""
    return render_template('documentation.html')

@app.route('/api/generate-workout', methods=['POST'])
def generate_workout():
    """
    API endpoint to generate a workout plan based on user profile.
    
    Expects a JSON object with the following fields:
    - name: string
    - age: integer
    - gender: string ("male", "female", "other")
    - goal: string ("muscle_gain", "weight_loss", "strength", "endurance")
    - experience: string ("beginner", "intermediate", "advanced")
    - equipment: array of strings
    - days_per_week: integer (1-7)
    - include_custom_section: boolean (optional)
    - custom_section_type: string ("circuit", "superset") (optional)
    
    Returns:
    - 200 OK: JSON workout plan
    - 400 Bad Request: Error message
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        # Validate the input data
        validation_result = validate_input(data)
        if not validation_result['valid']:
            return jsonify({"error": validation_result['message']}), 400
        
        # Generate the workout plan based on the user profile
        include_custom = data.get('include_custom_section', False)
        custom_type = data.get('custom_section_type', 'circuit') if include_custom else None
        
        workout_plan = generate_workout_plan(
            name=data.get('name'),
            age=data.get('age'),
            gender=data.get('gender'),
            goal=data.get('goal'),
            experience=data.get('experience'),
            equipment=data.get('equipment', []),
            days_per_week=data.get('days_per_week', 3),
            include_custom_section=include_custom,
            custom_section_type=custom_type
        )
        
        return jsonify(workout_plan)
    
    except Exception as e:
        logger.exception("Error generating workout plan")
        return jsonify({"error": str(e)}), 500

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "The requested URL was not found"}), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({"error": "Method not allowed"}), 405

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
