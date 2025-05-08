import datetime
import logging
import random
from exercise_data import (
    get_warmup_exercises,
    get_main_exercises,
    get_cooldown_exercises,
    get_circuit_exercises,
    get_superset_exercises
)

logger = logging.getLogger(__name__)

def generate_workout_plan(
    name, 
    age, 
    gender, 
    goal, 
    experience, 
    equipment, 
    days_per_week=3, 
    include_custom_section=False,
    custom_section_type="circuit"
):
    """
    Generate a 12-session workout plan based on user profile.
    
    Args:
        name (str): Client name
        age (int): Client age
        gender (str): Client gender
        goal (str): Training goal (muscle_gain, weight_loss, strength, endurance)
        experience (str): Training experience level (beginner, intermediate, advanced)
        equipment (list): Available equipment
        days_per_week (int): Training days per week
        include_custom_section (bool): Whether to include a custom section
        custom_section_type (str): Type of custom section (circuit, superset)
        
    Returns:
        dict: Complete workout plan with 12 sessions
    """
    logger.debug(f"Generating workout for {name}, goal: {goal}, experience: {experience}")
    
    # Initialize the workout plan
    workout_plan = {
        "client_profile": {
            "name": name,
            "age": age,
            "gender": gender,
            "goal": goal,
            "experience": experience,
            "equipment": equipment,
            "days_per_week": days_per_week
        },
        "sessions": []
    }
    
    # Determine split type based on goal and experience
    if goal == "muscle_gain" or goal == "strength":
        split_type = "push_pull_legs" if experience != "beginner" else "full_body"
    elif goal == "weight_loss":
        split_type = "full_body"
    else:  # endurance or other
        split_type = "upper_lower"
    
    logger.debug(f"Using split type: {split_type}")
    
    # Determine starting date (starting from next Monday)
    today = datetime.date.today()
    days_until_monday = (7 - today.weekday()) % 7
    start_date = today + datetime.timedelta(days=days_until_monday)
    
    # Determine training days based on days_per_week
    if days_per_week == 3:
        # Monday, Wednesday, Friday
        training_days = [0, 2, 4]  # 0 = Monday, 2 = Wednesday, 4 = Friday
    elif days_per_week == 4:
        # Monday, Tuesday, Thursday, Friday
        training_days = [0, 1, 3, 4]
    else:
        # Flexible for other day counts
        training_days = list(range(min(days_per_week, 7)))
    
    # Generate 12 sessions (4 weeks with days_per_week sessions per week)
    session_counter = 1
    for week in range(4):  # 4 weeks
        for day_idx in range(min(days_per_week, len(training_days))):
            # Calculate the date for this session
            days_offset = week * 7 + training_days[day_idx]
            session_date = start_date + datetime.timedelta(days=days_offset)
            
            # Determine the workout type for this session based on split_type
            if split_type == "push_pull_legs":
                if session_counter % 3 == 1:
                    workout_type = "push"
                elif session_counter % 3 == 2:
                    workout_type = "pull"
                else:
                    workout_type = "legs"
            elif split_type == "upper_lower":
                workout_type = "upper" if session_counter % 2 == 1 else "lower"
            else:  # full_body
                workout_type = "full_body"
            
            # Generate the session
            session = generate_session(
                session_number=session_counter,
                session_date=session_date.strftime("%Y-%m-%d"),
                workout_type=workout_type,
                week=week+1,
                goal=goal,
                experience=experience,
                equipment=equipment,
                include_custom_section=include_custom_section,
                custom_section_type=custom_section_type
            )
            
            workout_plan["sessions"].append(session)
            session_counter += 1
    
    return workout_plan

def generate_session(
    session_number, 
    session_date, 
    workout_type, 
    week, 
    goal, 
    experience, 
    equipment, 
    include_custom_section, 
    custom_section_type
):
    """
    Generate a single workout session.
    
    Args:
        session_number (int): Session number (1-12)
        session_date (str): Session date in ISO format
        workout_type (str): Type of workout (push, pull, legs, upper, lower, full_body)
        week (int): Week number (1-4)
        goal (str): Training goal
        experience (str): Experience level
        equipment (list): Available equipment
        include_custom_section (bool): Whether to include a custom section
        custom_section_type (str): Type of custom section
        
    Returns:
        dict: Complete workout session
    """
    # Initialize the session
    session = {
        "session": session_number,
        "date": session_date,
        "workout_type": workout_type,
        "week": week,
        "sections": {}
    }
    
    # Generate warm-up section
    warmup_exercises = get_warmup_exercises(workout_type, equipment)
    session["sections"]["warmup"] = select_and_format_exercises(
        warmup_exercises, 
        3, 
        "warmup"
    )
    
    # Generate main section with progressive overload
    main_exercises = get_main_exercises(workout_type, goal, experience, equipment)
    session["sections"]["main"] = select_and_format_exercises(
        main_exercises, 
        4 if experience == "beginner" else 5, 
        "main",
        apply_progression=True,
        week=week,
        experience=experience
    )
    
    # Generate custom section if requested
    if include_custom_section:
        if custom_section_type == "circuit":
            custom_exercises = get_circuit_exercises(workout_type, goal, equipment)
            session["sections"]["circuit"] = select_and_format_exercises(
                custom_exercises, 
                4, 
                "circuit"
            )
        elif custom_section_type == "superset":
            custom_exercises = get_superset_exercises(workout_type, goal, equipment)
            session["sections"]["superset"] = select_and_format_exercises(
                custom_exercises, 
                2, 
                "superset"
            )
    
    # Generate cool-down section
    cooldown_exercises = get_cooldown_exercises(workout_type)
    session["sections"]["cooldown"] = select_and_format_exercises(
        cooldown_exercises, 
        3, 
        "cooldown"
    )
    
    return session

def select_and_format_exercises(exercises, count, section_type, apply_progression=False, week=1, experience="beginner"):
    """
    Select exercises from a list and format them with appropriate parameters.
    
    Args:
        exercises (list): List of exercises to choose from
        count (int): Number of exercises to select
        section_type (str): Section type (warmup, main, cooldown, circuit, superset)
        apply_progression (bool): Whether to apply progressive overload
        week (int): Week number for progressive overload
        experience (str): Experience level
        
    Returns:
        list: Formatted exercise list
    """
    # Select exercises
    if len(exercises) <= count:
        selected_exercises = exercises.copy()
    else:
        selected_exercises = random.sample(exercises, count)
    
    # Format exercises based on section type
    formatted_exercises = []
    
    for exercise in selected_exercises:
        if section_type == "warmup":
            if "cardio" in exercise.get("type", []):
                formatted_exercise = {
                    "name": exercise["name"],
                    "duration": f"{2 + (week-1) * 0.5} min"
                }
            else:
                formatted_exercise = {
                    "name": exercise["name"],
                    "sets": 1 if week == 1 else 2,
                    "reps": 10 + (week-1) * 2
                }
                
        elif section_type == "main":
            base_reps = exercise.get("base_reps", 10)
            base_sets = exercise.get("base_sets", 3)
            
            # Apply progressive overload based on week and experience
            if apply_progression:
                if experience == "beginner":
                    sets = base_sets
                    reps = base_reps + (week-1) * 2
                elif experience == "intermediate":
                    sets = base_sets + (week-1) // 2
                    reps = base_reps + ((week-1) % 2) * 2
                else:  # advanced
                    sets = base_sets + (week-1)
                    reps = base_reps
            else:
                sets = base_sets
                reps = base_reps
                
            # Rest time based on goal and experience
            if "strength" in exercise.get("primary_goal", []):
                rest = "90s" if experience == "advanced" else "75s"
            else:
                rest = "60s" if experience == "advanced" else "45s"
                
            # Tempo based on goal
            tempo = "2-0-1" if "endurance" in exercise.get("primary_goal", []) else "3-1-2"
            
            formatted_exercise = {
                "name": exercise["name"],
                "sets": sets,
                "reps": reps,
                "rest": rest,
                "tempo": tempo
            }
            
        elif section_type == "cooldown":
            formatted_exercise = {
                "name": exercise["name"],
                "duration": f"{30 + (week-1) * 10} sec each side" if "each side" in exercise.get("notes", "") else f"{45 + (week-1) * 15} sec"
            }
            
        elif section_type == "circuit":
            formatted_exercise = {
                "name": exercise["name"],
                "time": f"{30 + (week-1) * 5} sec",
                "rounds": 3
            }
            
        elif section_type == "superset":
            formatted_exercise = {
                "name": exercise["name"],
                "sets": 3,
                "reps": 12,
                "no_rest": True
            }
            
        formatted_exercises.append(formatted_exercise)
    
    return formatted_exercises
