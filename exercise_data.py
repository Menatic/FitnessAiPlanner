"""
Exercise database for the workout generator.
Each exercise has metadata including:
- name: Exercise name
- type: List of categories (e.g., "compound", "isolation", "cardio", "stretch")
- muscle_group: Primary muscle group targeted
- secondary_muscles: Secondary muscles targeted
- equipment: Required equipment
- difficulty: Beginner, intermediate, or advanced
- primary_goal: What this exercise is best for (strength, hypertrophy, endurance)
- base_sets: Default number of sets
- base_reps: Default number of reps
- notes: Additional notes or instructions
"""

# Warm-up exercises database
WARMUP_EXERCISES = [
    # Cardio warm-ups
    {
        "name": "Jumping Jacks",
        "type": ["cardio", "dynamic"],
        "equipment": [],
        "difficulty": "beginner"
    },
    {
        "name": "High Knees",
        "type": ["cardio", "dynamic"],
        "equipment": [],
        "difficulty": "beginner"
    },
    {
        "name": "Arm Circles",
        "type": ["dynamic", "mobility"],
        "muscle_group": "shoulders",
        "equipment": [],
        "difficulty": "beginner"
    },
    {
        "name": "Leg Swings",
        "type": ["dynamic", "mobility"],
        "muscle_group": "hips",
        "equipment": [],
        "difficulty": "beginner",
        "notes": "each side"
    },
    {
        "name": "Walking Lunges",
        "type": ["dynamic", "compound"],
        "muscle_group": "legs",
        "equipment": [],
        "difficulty": "beginner"
    },
    {
        "name": "Bodyweight Squats",
        "type": ["dynamic", "compound"],
        "muscle_group": "legs",
        "equipment": [],
        "difficulty": "beginner"
    },
    {
        "name": "Hip Circles",
        "type": ["dynamic", "mobility"],
        "muscle_group": "hips",
        "equipment": [],
        "difficulty": "beginner"
    },
    {
        "name": "Shoulder Rotations",
        "type": ["dynamic", "mobility"],
        "muscle_group": "shoulders",
        "equipment": [],
        "difficulty": "beginner"
    },
    {
        "name": "March in Place",
        "type": ["cardio", "dynamic"],
        "equipment": [],
        "difficulty": "beginner"
    },
    {
        "name": "Torso Twists",
        "type": ["dynamic", "mobility"],
        "muscle_group": "core",
        "equipment": [],
        "difficulty": "beginner"
    },
    {
        "name": "Resistance Band Pull-Aparts",
        "type": ["dynamic", "mobility"],
        "muscle_group": "shoulders",
        "equipment": ["resistance_band"],
        "difficulty": "beginner"
    }
]

# Main exercises database
MAIN_EXERCISES = [
    # Push exercises (chest, shoulders, triceps)
    {
        "name": "Dumbbell Chest Press",
        "type": ["compound"],
        "muscle_group": "chest",
        "secondary_muscles": ["shoulders", "triceps"],
        "equipment": ["dumbbells", "bench"],
        "difficulty": "beginner",
        "primary_goal": ["strength", "hypertrophy"],
        "base_sets": 3,
        "base_reps": 10
    },
    {
        "name": "Push-Ups",
        "type": ["compound"],
        "muscle_group": "chest",
        "secondary_muscles": ["shoulders", "triceps", "core"],
        "equipment": [],
        "difficulty": "beginner",
        "primary_goal": ["strength", "endurance"],
        "base_sets": 3,
        "base_reps": 12
    },
    {
        "name": "Dumbbell Shoulder Press",
        "type": ["compound"],
        "muscle_group": "shoulders",
        "secondary_muscles": ["triceps"],
        "equipment": ["dumbbells"],
        "difficulty": "beginner",
        "primary_goal": ["strength", "hypertrophy"],
        "base_sets": 3,
        "base_reps": 10
    },
    {
        "name": "Dumbbell Lateral Raises",
        "type": ["isolation"],
        "muscle_group": "shoulders",
        "equipment": ["dumbbells"],
        "difficulty": "beginner",
        "primary_goal": ["hypertrophy"],
        "base_sets": 3,
        "base_reps": 12
    },
    {
        "name": "Dumbbell Tricep Extensions",
        "type": ["isolation"],
        "muscle_group": "triceps",
        "equipment": ["dumbbells"],
        "difficulty": "beginner",
        "primary_goal": ["hypertrophy"],
        "base_sets": 3,
        "base_reps": 12
    },
    {
        "name": "Resistance Band Chest Fly",
        "type": ["isolation"],
        "muscle_group": "chest",
        "secondary_muscles": ["shoulders"],
        "equipment": ["resistance_band"],
        "difficulty": "beginner",
        "primary_goal": ["hypertrophy", "endurance"],
        "base_sets": 3,
        "base_reps": 15
    },
    {
        "name": "Dumbbell Floor Press",
        "type": ["compound"],
        "muscle_group": "chest",
        "secondary_muscles": ["triceps", "shoulders"],
        "equipment": ["dumbbells"],
        "difficulty": "intermediate",
        "primary_goal": ["strength", "hypertrophy"],
        "base_sets": 4,
        "base_reps": 8
    },
    {
        "name": "Resistance Band Tricep Pushdown",
        "type": ["isolation"],
        "muscle_group": "triceps",
        "equipment": ["resistance_band"],
        "difficulty": "beginner",
        "primary_goal": ["hypertrophy", "endurance"],
        "base_sets": 3,
        "base_reps": 15
    },
    {
        "name": "Dumbbell Incline Press",
        "type": ["compound"],
        "muscle_group": "chest",
        "secondary_muscles": ["shoulders", "triceps"],
        "equipment": ["dumbbells", "bench"],
        "difficulty": "intermediate",
        "primary_goal": ["strength", "hypertrophy"],
        "base_sets": 3,
        "base_reps": 10
    },

    # Pull exercises (back, biceps)
    {
        "name": "Dumbbell Rows",
        "type": ["compound"],
        "muscle_group": "back",
        "secondary_muscles": ["biceps", "shoulders"],
        "equipment": ["dumbbells", "bench"],
        "difficulty": "beginner",
        "primary_goal": ["strength", "hypertrophy"],
        "base_sets": 3,
        "base_reps": 10
    },
    {
        "name": "Resistance Band Row",
        "type": ["compound"],
        "muscle_group": "back",
        "secondary_muscles": ["biceps", "shoulders"],
        "equipment": ["resistance_band"],
        "difficulty": "beginner",
        "primary_goal": ["strength", "endurance"],
        "base_sets": 3,
        "base_reps": 12
    },
    {
        "name": "Dumbbell Bicep Curls",
        "type": ["isolation"],
        "muscle_group": "biceps",
        "equipment": ["dumbbells"],
        "difficulty": "beginner",
        "primary_goal": ["hypertrophy"],
        "base_sets": 3,
        "base_reps": 12
    },
    {
        "name": "Resistance Band Bicep Curls",
        "type": ["isolation"],
        "muscle_group": "biceps",
        "equipment": ["resistance_band"],
        "difficulty": "beginner",
        "primary_goal": ["hypertrophy", "endurance"],
        "base_sets": 3,
        "base_reps": 15
    },
    {
        "name": "Dumbbell Pullover",
        "type": ["compound"],
        "muscle_group": "back",
        "secondary_muscles": ["chest", "triceps"],
        "equipment": ["dumbbells", "bench"],
        "difficulty": "intermediate",
        "primary_goal": ["hypertrophy"],
        "base_sets": 3,
        "base_reps": 10
    },
    {
        "name": "Dumbbell Reverse Fly",
        "type": ["isolation"],
        "muscle_group": "upper_back",
        "secondary_muscles": ["shoulders"],
        "equipment": ["dumbbells"],
        "difficulty": "beginner",
        "primary_goal": ["hypertrophy", "endurance"],
        "base_sets": 3,
        "base_reps": 12
    },
    {
        "name": "Resistance Band Pull-Aparts",
        "type": ["isolation"],
        "muscle_group": "upper_back",
        "secondary_muscles": ["shoulders"],
        "equipment": ["resistance_band"],
        "difficulty": "beginner",
        "primary_goal": ["endurance", "hypertrophy"],
        "base_sets": 3,
        "base_reps": 15
    },
    {
        "name": "Dumbbell Hammer Curls",
        "type": ["isolation"],
        "muscle_group": "biceps",
        "secondary_muscles": ["forearms"],
        "equipment": ["dumbbells"],
        "difficulty": "beginner",
        "primary_goal": ["hypertrophy"],
        "base_sets": 3,
        "base_reps": 12
    },

    # Leg exercises
    {
        "name": "Dumbbell Goblet Squats",
        "type": ["compound"],
        "muscle_group": "quads",
        "secondary_muscles": ["glutes", "hamstrings", "core"],
        "equipment": ["dumbbells"],
        "difficulty": "beginner",
        "primary_goal": ["strength", "hypertrophy"],
        "base_sets": 3,
        "base_reps": 12
    },
    {
        "name": "Dumbbell Walking Lunges",
        "type": ["compound"],
        "muscle_group": "quads",
        "secondary_muscles": ["glutes", "hamstrings", "core"],
        "equipment": ["dumbbells"],
        "difficulty": "intermediate",
        "primary_goal": ["strength", "hypertrophy"],
        "base_sets": 3,
        "base_reps": 10
    },
    {
        "name": "Dumbbell Romanian Deadlifts",
        "type": ["compound"],
        "muscle_group": "hamstrings",
        "secondary_muscles": ["glutes", "lower_back"],
        "equipment": ["dumbbells"],
        "difficulty": "intermediate",
        "primary_goal": ["strength", "hypertrophy"],
        "base_sets": 3,
        "base_reps": 10
    },
    {
        "name": "Resistance Band Glute Bridges",
        "type": ["compound"],
        "muscle_group": "glutes",
        "secondary_muscles": ["hamstrings"],
        "equipment": ["resistance_band"],
        "difficulty": "beginner",
        "primary_goal": ["strength", "hypertrophy"],
        "base_sets": 3,
        "base_reps": 15
    },
    {
        "name": "Bodyweight Squats",
        "type": ["compound"],
        "muscle_group": "quads",
        "secondary_muscles": ["glutes", "hamstrings", "core"],
        "equipment": [],
        "difficulty": "beginner",
        "primary_goal": ["endurance", "strength"],
        "base_sets": 3,
        "base_reps": 15
    },
    {
        "name": "Resistance Band Standing Leg Curls",
        "type": ["isolation"],
        "muscle_group": "hamstrings",
        "equipment": ["resistance_band"],
        "difficulty": "beginner",
        "primary_goal": ["endurance", "hypertrophy"],
        "base_sets": 3,
        "base_reps": 12
    },
    {
        "name": "Dumbbell Step-Ups",
        "type": ["compound"],
        "muscle_group": "quads",
        "secondary_muscles": ["glutes", "hamstrings"],
        "equipment": ["dumbbells", "bench"],
        "difficulty": "intermediate",
        "primary_goal": ["strength", "hypertrophy"],
        "base_sets": 3,
        "base_reps": 10
    },
    {
        "name": "Dumbbell Calf Raises",
        "type": ["isolation"],
        "muscle_group": "calves",
        "equipment": ["dumbbells"],
        "difficulty": "beginner",
        "primary_goal": ["hypertrophy", "endurance"],
        "base_sets": 3,
        "base_reps": 15
    },

    # Core exercises
    {
        "name": "Plank",
        "type": ["isometric"],
        "muscle_group": "core",
        "equipment": [],
        "difficulty": "beginner",
        "primary_goal": ["endurance", "strength"],
        "base_sets": 3,
        "base_reps": 30
    },
    {
        "name": "Russian Twists",
        "type": ["isolation"],
        "muscle_group": "obliques",
        "secondary_muscles": ["core"],
        "equipment": ["dumbbells"],
        "difficulty": "beginner",
        "primary_goal": ["strength", "endurance"],
        "base_sets": 3,
        "base_reps": 12
    },
    {
        "name": "Bicycle Crunches",
        "type": ["isolation"],
        "muscle_group": "core",
        "secondary_muscles": ["obliques"],
        "equipment": [],
        "difficulty": "beginner",
        "primary_goal": ["endurance", "hypertrophy"],
        "base_sets": 3,
        "base_reps": 15
    },
    {
        "name": "Mountain Climbers",
        "type": ["compound", "cardio"],
        "muscle_group": "core",
        "secondary_muscles": ["shoulders", "chest", "quads"],
        "equipment": [],
        "difficulty": "beginner",
        "primary_goal": ["endurance"],
        "base_sets": 3,
        "base_reps": 20
    }
]

# Cool-down exercises database
COOLDOWN_EXERCISES = [
    {
        "name": "Child's Pose",
        "type": ["static", "stretch"],
        "muscle_group": "back",
        "secondary_muscles": ["shoulders"],
        "equipment": [],
        "difficulty": "beginner"
    },
    {
        "name": "Lying Hamstring Stretch",
        "type": ["static", "stretch"],
        "muscle_group": "hamstrings",
        "equipment": [],
        "difficulty": "beginner",
        "notes": "each side"
    },
    {
        "name": "Chest Stretch",
        "type": ["static", "stretch"],
        "muscle_group": "chest",
        "secondary_muscles": ["shoulders"],
        "equipment": [],
        "difficulty": "beginner",
        "notes": "each side"
    },
    {
        "name": "Seated Forward Bend",
        "type": ["static", "stretch"],
        "muscle_group": "hamstrings",
        "secondary_muscles": ["lower_back"],
        "equipment": [],
        "difficulty": "beginner"
    },
    {
        "name": "Cross-Body Shoulder Stretch",
        "type": ["static", "stretch"],
        "muscle_group": "shoulders",
        "equipment": [],
        "difficulty": "beginner",
        "notes": "each side"
    },
    {
        "name": "Butterfly Stretch",
        "type": ["static", "stretch"],
        "muscle_group": "hips",
        "secondary_muscles": ["groin"],
        "equipment": [],
        "difficulty": "beginner"
    },
    {
        "name": "Cobra Pose",
        "type": ["static", "stretch"],
        "muscle_group": "abs",
        "secondary_muscles": ["chest", "shoulders"],
        "equipment": [],
        "difficulty": "beginner"
    },
    {
        "name": "Standing Quadriceps Stretch",
        "type": ["static", "stretch"],
        "muscle_group": "quads",
        "equipment": [],
        "difficulty": "beginner",
        "notes": "each side"
    },
    {
        "name": "Tricep Stretch",
        "type": ["static", "stretch"],
        "muscle_group": "triceps",
        "equipment": [],
        "difficulty": "beginner",
        "notes": "each side"
    },
    {
        "name": "Cat-Cow Stretch",
        "type": ["dynamic", "stretch"],
        "muscle_group": "spine",
        "secondary_muscles": ["core", "back"],
        "equipment": [],
        "difficulty": "beginner"
    }
]

# Circuit exercises database
CIRCUIT_EXERCISES = [
    {
        "name": "Jumping Jacks",
        "type": ["cardio"],
        "equipment": [],
        "difficulty": "beginner"
    },
    {
        "name": "Mountain Climbers",
        "type": ["cardio", "core"],
        "equipment": [],
        "difficulty": "beginner"
    },
    {
        "name": "Bodyweight Squats",
        "type": ["compound", "legs"],
        "equipment": [],
        "difficulty": "beginner"
    },
    {
        "name": "Push-Ups",
        "type": ["compound", "push"],
        "equipment": [],
        "difficulty": "beginner"
    },
    {
        "name": "High Knees",
        "type": ["cardio"],
        "equipment": [],
        "difficulty": "beginner"
    },
    {
        "name": "Plank",
        "type": ["core", "isometric"],
        "equipment": [],
        "difficulty": "beginner"
    },
    {
        "name": "Resistance Band Rows",
        "type": ["compound", "pull"],
        "equipment": ["resistance_band"],
        "difficulty": "beginner"
    },
    {
        "name": "Bicycle Crunches",
        "type": ["core"],
        "equipment": [],
        "difficulty": "beginner"
    },
    {
        "name": "Dumbbell Goblet Squats",
        "type": ["compound", "legs"],
        "equipment": ["dumbbells"],
        "difficulty": "beginner"
    },
    {
        "name": "Lateral Shuffles",
        "type": ["cardio", "agility"],
        "equipment": [],
        "difficulty": "beginner"
    }
]

# Superset exercises database
SUPERSET_EXERCISES = [
    # Push-Pull Supersets
    {
        "name": "Dumbbell Chest Press + Dumbbell Rows",
        "type": ["compound", "superset"],
        "muscle_group": "push_pull",
        "equipment": ["dumbbells", "bench"],
        "difficulty": "intermediate"
    },
    {
        "name": "Push-Ups + Resistance Band Rows",
        "type": ["compound", "superset"],
        "muscle_group": "push_pull",
        "equipment": ["resistance_band"],
        "difficulty": "beginner"
    },
    {
        "name": "Dumbbell Shoulder Press + Dumbbell Bicep Curls",
        "type": ["compound", "isolation", "superset"],
        "muscle_group": "push_pull",
        "equipment": ["dumbbells"],
        "difficulty": "beginner"
    },
    
    # Upper-Lower Supersets
    {
        "name": "Dumbbell Goblet Squats + Push-Ups",
        "type": ["compound", "superset"],
        "muscle_group": "upper_lower",
        "equipment": ["dumbbells"],
        "difficulty": "beginner"
    },
    {
        "name": "Dumbbell Romanian Deadlifts + Dumbbell Rows",
        "type": ["compound", "superset"],
        "muscle_group": "upper_lower",
        "equipment": ["dumbbells"],
        "difficulty": "intermediate"
    },
    
    # Antagonist Supersets
    {
        "name": "Dumbbell Bicep Curls + Resistance Band Tricep Extensions",
        "type": ["isolation", "superset"],
        "muscle_group": "arms",
        "equipment": ["dumbbells", "resistance_band"],
        "difficulty": "beginner"
    },
    {
        "name": "Dumbbell Lateral Raises + Dumbbell Reverse Fly",
        "type": ["isolation", "superset"],
        "muscle_group": "shoulders",
        "equipment": ["dumbbells"],
        "difficulty": "beginner"
    }
]

def get_warmup_exercises(workout_type, equipment):
    """Get warm-up exercises based on workout type and available equipment."""
    compatible_exercises = []
    
    for exercise in WARMUP_EXERCISES:
        # Check if exercise requires equipment that's available
        equipment_required = exercise.get("equipment", [])
        if all(item in equipment for item in equipment_required) or not equipment_required:
            compatible_exercises.append(exercise)
    
    return compatible_exercises

def get_main_exercises(workout_type, goal, experience, equipment):
    """Get main exercises based on workout type, goal, and available equipment."""
    compatible_exercises = []
    
    for exercise in MAIN_EXERCISES:
        # Check if exercise is appropriate for workout type
        if workout_type == "push" and exercise.get("muscle_group") in ["chest", "shoulders", "triceps"]:
            pass
        elif workout_type == "pull" and exercise.get("muscle_group") in ["back", "biceps"]:
            pass
        elif workout_type == "legs" and exercise.get("muscle_group") in ["quads", "hamstrings", "glutes", "calves"]:
            pass
        elif workout_type == "upper" and exercise.get("muscle_group") in ["chest", "back", "shoulders", "biceps", "triceps"]:
            pass
        elif workout_type == "lower" and exercise.get("muscle_group") in ["quads", "hamstrings", "glutes", "calves"]:
            pass
        elif workout_type == "full_body":
            pass
        else:
            continue
        
        # Check if exercise requires equipment that's available
        equipment_required = exercise.get("equipment", [])
        if all(item in equipment for item in equipment_required) or not equipment_required:
            # Check if exercise matches experience level
            if experience == "beginner" and exercise.get("difficulty") == "beginner":
                compatible_exercises.append(exercise)
            elif experience == "intermediate" and exercise.get("difficulty") in ["beginner", "intermediate"]:
                compatible_exercises.append(exercise)
            elif experience == "advanced":
                compatible_exercises.append(exercise)
    
    return compatible_exercises

def get_cooldown_exercises(workout_type):
    """Get cool-down exercises based on workout type."""
    return COOLDOWN_EXERCISES

def get_circuit_exercises(workout_type, goal, equipment):
    """Get circuit exercises based on workout type, goal, and available equipment."""
    compatible_exercises = []
    
    for exercise in CIRCUIT_EXERCISES:
        # Check if exercise requires equipment that's available
        equipment_required = exercise.get("equipment", [])
        if all(item in equipment for item in equipment_required) or not equipment_required:
            compatible_exercises.append(exercise)
    
    return compatible_exercises

def get_superset_exercises(workout_type, goal, equipment):
    """Get superset exercises based on workout type, goal, and available equipment."""
    compatible_exercises = []
    
    for exercise in SUPERSET_EXERCISES:
        # Check if superset is appropriate for workout type
        if workout_type == "push" and "push_pull" in exercise.get("muscle_group", ""):
            pass
        elif workout_type == "pull" and "push_pull" in exercise.get("muscle_group", ""):
            pass
        elif workout_type == "legs" and "upper_lower" in exercise.get("muscle_group", ""):
            pass
        elif workout_type == "upper" and ("push_pull" in exercise.get("muscle_group", "") or "arms" in exercise.get("muscle_group", "") or "shoulders" in exercise.get("muscle_group", "")):
            pass
        elif workout_type == "lower" and "upper_lower" in exercise.get("muscle_group", ""):
            pass
        elif workout_type == "full_body":
            pass
        else:
            continue
        
        # Check if superset requires equipment that's available
        equipment_required = exercise.get("equipment", [])
        if all(item in equipment for item in equipment_required) or not equipment_required:
            compatible_exercises.append(exercise)
    
    return compatible_exercises
