"""
Utility functions for the workout plan generator.
"""

def validate_input(data):
    """
    Validate the input data for generating a workout plan.
    
    Args:
        data (dict): Input data for workout generation
        
    Returns:
        dict: Validation result with 'valid' and 'message' keys
    """
    # Check required fields
    required_fields = ['name', 'age', 'gender', 'goal', 'experience', 'equipment', 'days_per_week']
    for field in required_fields:
        if field not in data:
            return {
                'valid': False,
                'message': f"Missing required field: {field}"
            }
    
    # Validate age
    if not isinstance(data.get('age'), int) or data.get('age') < 16 or data.get('age') > 80:
        return {
            'valid': False,
            'message': "Age must be an integer between 16 and 80"
        }
    
    # Validate gender
    valid_genders = ['male', 'female', 'other']
    if data.get('gender').lower() not in valid_genders:
        return {
            'valid': False,
            'message': f"Gender must be one of: {', '.join(valid_genders)}"
        }
    
    # Validate goal
    valid_goals = ['muscle_gain', 'weight_loss', 'strength', 'endurance']
    if data.get('goal').lower() not in valid_goals:
        return {
            'valid': False,
            'message': f"Goal must be one of: {', '.join(valid_goals)}"
        }
    
    # Validate experience
    valid_experience_levels = ['beginner', 'intermediate', 'advanced']
    if data.get('experience').lower() not in valid_experience_levels:
        return {
            'valid': False,
            'message': f"Experience must be one of: {', '.join(valid_experience_levels)}"
        }
    
    # Validate equipment
    if not isinstance(data.get('equipment'), list):
        return {
            'valid': False,
            'message': "Equipment must be a list"
        }
    
    # Validate days_per_week
    if not isinstance(data.get('days_per_week'), int) or data.get('days_per_week') < 1 or data.get('days_per_week') > 7:
        return {
            'valid': False,
            'message': "Days per week must be an integer between 1 and 7"
        }
    
    # Validate optional fields
    if 'include_custom_section' in data and not isinstance(data.get('include_custom_section'), bool):
        return {
            'valid': False,
            'message': "include_custom_section must be a boolean"
        }
    
    if 'custom_section_type' in data:
        valid_section_types = ['circuit', 'superset']
        if data.get('custom_section_type').lower() not in valid_section_types:
            return {
                'valid': False,
                'message': f"Custom section type must be one of: {', '.join(valid_section_types)}"
            }
    
    return {
        'valid': True,
        'message': "Input is valid"
    }
