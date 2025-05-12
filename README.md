# Fitness AI Planner 🤖💪

An intelligent workout planning system that generates personalized 12-session fitness programs using AI-driven recommendations.

To view the live project on Render -> https://fitnessaiplanner.onrender.com/

## Features ✨
- **AI-Powered Workout Generation** - Creates customized plans based on user goals (muscle gain, weight loss, strength, endurance)
- **Dynamic Programming Logic** - Implements push/pull/legs, upper/lower, and full-body splits
- **Progressive Overload System** - Automatically increases intensity over 4 weeks
- **Equipment Customization** - Generates plans based on available equipment
- **Interactive Web UI** - Modern dashboard with workout visualization
- **PDF Export** - Printable workout plans with exercise details

## Installation ⚙️
```bash
# Clone repository
git clone https://github.com/Menatic/FitnessAiPlanner.git
cd FitnessAiPlanner

# Create virtual environment (Windows)
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
flask run
```

## Usage 🚀

1. Access the web interface at http://localhost:5000
2. Fill in user profile:
   - Training experience level
   - Fitness goals
   - Available equipment
3. Generate and view interactive workout plan
4. Export PDF for offline use


## Project Structure 📁

```graphsql
FitnessAiPlanner/
├── app.py                   # Core Flask application
├── workout_generator.py     # AI-based workout plan generator
├── exercise_data.py         # Contains exercise metadata/database
├── requirements.txt         # Project dependencies
├── README.md                # Project documentation

├── templates/               # HTML templates rendered by Flask
│   ├── index.html           # Main landing page
│   ├── documentation.html   # API documentation page
│   └── workout_plan.html    # Generated workout plan view

├── static/                  # Static frontend assets
│   ├── css/
│   │   └── styles.css       # Custom CSS styling
│   └── js/
│       └── main.js          # JavaScript for interactive features
```

## Contributing 🤝
1. Fork the repository
2. Create feature branch ( git checkout -b feature/amazing-feature )
3. Commit changes ( git commit -m 'Add amazing feature' )
4. Push to branch ( git push origin feature/amazing-feature )
5. Open Pull Request

Disclaimer: This application provides workout suggestions only. Consult a healthcare professional before starting any new exercise program.
