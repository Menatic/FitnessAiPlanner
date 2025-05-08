/**
 * Workout Plan Generator - Client-side JavaScript
 * Handles form submission and displaying API results
 */

document.addEventListener('DOMContentLoaded', function() {
    // Get form and result elements
    const workoutForm = document.getElementById('workoutForm');
    const resultContainer = document.getElementById('resultContainer');
    const workoutResult = document.getElementById('workoutResult');
    const loadingSpinner = document.getElementById('loadingSpinner');
    const errorAlert = document.getElementById('errorAlert');
    const errorMessage = document.getElementById('errorMessage');
    
    // Equipment options that can be selected
    const equipmentOptions = [
        'dumbbells', 
        'bench', 
        'resistance_band', 
        'barbell', 
        'kettlebell', 
        'medicine_ball', 
        'pull_up_bar'
    ];
    
    // Populate equipment checkboxes dynamically
    const equipmentContainer = document.getElementById('equipmentContainer');
    if (equipmentContainer) {
        equipmentOptions.forEach(equipment => {
            const div = document.createElement('div');
            div.className = 'form-check form-check-inline';
            
            const input = document.createElement('input');
            input.className = 'form-check-input';
            input.type = 'checkbox';
            input.id = `equipment_${equipment}`;
            input.name = 'equipment';
            input.value = equipment;
            
            const label = document.createElement('label');
            label.className = 'form-check-label';
            label.htmlFor = `equipment_${equipment}`;
            label.textContent = equipment.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase());
            
            div.appendChild(input);
            div.appendChild(label);
            equipmentContainer.appendChild(div);
        });
    }
    
    // Handle form submission
    if (workoutForm) {
        workoutForm.addEventListener('submit', function(event) {
            event.preventDefault();
            
            // Show loading spinner and hide previous results/errors
            loadingSpinner.classList.remove('d-none');
            resultContainer.classList.add('d-none');
            errorAlert.classList.add('d-none');
            
            // Get form data
            const formData = new FormData(workoutForm);
            
            // Create request payload
            const payload = {
                name: formData.get('name'),
                age: parseInt(formData.get('age')),
                gender: formData.get('gender'),
                goal: formData.get('goal'),
                experience: formData.get('experience'),
                equipment: Array.from(formData.getAll('equipment')),
                days_per_week: parseInt(formData.get('days_per_week')),
                include_custom_section: formData.get('include_custom_section') === 'on',
                custom_section_type: formData.get('custom_section_type')
            };
            
            // Send API request
            fetch('/api/generate-workout', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            })
            .then(response => {
                if (!response.ok) {
                    return response.json().then(data => {
                        throw new Error(data.error || 'An error occurred');
                    });
                }
                return response.json();
            })
            .then(data => {
                // Display the results
                displayWorkoutPlan(data);
                resultContainer.classList.remove('d-none');
                loadingSpinner.classList.add('d-none');
            })
            .catch(error => {
                // Display error message
                errorMessage.textContent = error.message;
                errorAlert.classList.remove('d-none');
                loadingSpinner.classList.add('d-none');
                console.error('Error:', error);
            });
        });
    }
    
    // Toggle custom section options based on checkbox
    const customSectionCheckbox = document.getElementById('include_custom_section');
    const customSectionOptions = document.getElementById('customSectionOptions');
    
    if (customSectionCheckbox && customSectionOptions) {
        customSectionCheckbox.addEventListener('change', function() {
            if (this.checked) {
                customSectionOptions.classList.remove('d-none');
            } else {
                customSectionOptions.classList.add('d-none');
            }
        });
    }
    
    /**
     * Display the workout plan in the result container
     * @param {Object} workoutPlan - The workout plan data from the API
     */
    function displayWorkoutPlan(workoutPlan) {
        // Clear previous results
        workoutResult.innerHTML = '';
        
        // Create client profile summary
        const profileSummary = document.createElement('div');
        profileSummary.className = 'mb-4';
        profileSummary.innerHTML = `
            <h3>Workout Plan for ${workoutPlan.client_profile.name}</h3>
            <p><strong>Age:</strong> ${workoutPlan.client_profile.age} | 
               <strong>Gender:</strong> ${workoutPlan.client_profile.gender} | 
               <strong>Goal:</strong> ${formatGoal(workoutPlan.client_profile.goal)} | 
               <strong>Experience:</strong> ${capitalizeFirstLetter(workoutPlan.client_profile.experience)}</p>
        `;
        workoutResult.appendChild(profileSummary);
        
        // Create accordion for all sessions
        const accordion = document.createElement('div');
        accordion.className = 'accordion';
        accordion.id = 'sessionsAccordion';
        
        // Add each session to the accordion
        workoutPlan.sessions.forEach((session, index) => {
            const sessionId = `session-${index}`;
            const sessionDiv = document.createElement('div');
            sessionDiv.className = 'accordion-item mb-3';
            
            // Session header
            sessionDiv.innerHTML = `
                <h2 class="accordion-header" id="heading-${sessionId}">
                    <button class="accordion-button ${index > 0 ? 'collapsed' : ''}" type="button" 
                            data-bs-toggle="collapse" data-bs-target="#collapse-${sessionId}" 
                            aria-expanded="${index === 0 ? 'true' : 'false'}" aria-controls="collapse-${sessionId}">
                        Session ${session.session} - ${session.date} | ${capitalizeFirstLetter(session.workout_type)} Day | Week ${session.week}
                    </button>
                </h2>
            `;
            
            // Session content
            const sessionContentDiv = document.createElement('div');
            sessionContentDiv.id = `collapse-${sessionId}`;
            sessionContentDiv.className = `accordion-collapse collapse ${index === 0 ? 'show' : ''}`;
            sessionContentDiv.setAttribute('aria-labelledby', `heading-${sessionId}`);
            sessionContentDiv.setAttribute('data-bs-parent', '#sessionsAccordion');
            
            // Create the content for each section of the workout
            const sectionsContent = document.createElement('div');
            sectionsContent.className = 'accordion-body';
            
            // Warm-up section
            if (session.sections.warmup && session.sections.warmup.length > 0) {
                sectionsContent.appendChild(createSectionElement('Warm-up', session.sections.warmup));
            }
            
            // Main exercises section
            if (session.sections.main && session.sections.main.length > 0) {
                sectionsContent.appendChild(createSectionElement('Main Exercises', session.sections.main));
            }
            
            // Custom section (circuit or superset) if present
            if (session.sections.circuit && session.sections.circuit.length > 0) {
                sectionsContent.appendChild(createSectionElement('Circuit', session.sections.circuit));
            }
            
            if (session.sections.superset && session.sections.superset.length > 0) {
                sectionsContent.appendChild(createSectionElement('Superset', session.sections.superset));
            }
            
            // Cool-down section
            if (session.sections.cooldown && session.sections.cooldown.length > 0) {
                sectionsContent.appendChild(createSectionElement('Cool-down', session.sections.cooldown));
            }
            
            sessionContentDiv.appendChild(sectionsContent);
            sessionDiv.appendChild(sessionContentDiv);
            accordion.appendChild(sessionDiv);
        });
        
        workoutResult.appendChild(accordion);
    }
    
    /**
     * Create a section element for a workout section (warm-up, main, etc.)
     * @param {string} title - Section title
     * @param {Array} exercises - List of exercises in the section
     * @returns {HTMLElement} The section element
     */
    function createSectionElement(title, exercises) {
        const sectionDiv = document.createElement('div');
        sectionDiv.className = 'mb-4';
        
        // Section title
        const sectionTitle = document.createElement('h4');
        sectionTitle.className = 'mb-3';
        sectionTitle.textContent = title;
        sectionDiv.appendChild(sectionTitle);
        
        // Exercise table
        const table = document.createElement('table');
        table.className = 'table table-bordered table-hover';
        
        // Table headers
        const thead = document.createElement('thead');
        const headerRow = document.createElement('tr');
        
        // Determine columns based on first exercise's properties
        const columns = ['Exercise'];
        const firstExercise = exercises[0];
        
        if (firstExercise.sets) columns.push('Sets');
        if (firstExercise.reps) columns.push('Reps');
        if (firstExercise.duration) columns.push('Duration');
        if (firstExercise.rest) columns.push('Rest');
        if (firstExercise.tempo) columns.push('Tempo');
        if (firstExercise.time) columns.push('Time');
        if (firstExercise.rounds) columns.push('Rounds');
        
        // Create header cells
        columns.forEach(column => {
            const th = document.createElement('th');
            th.textContent = column;
            headerRow.appendChild(th);
        });
        
        thead.appendChild(headerRow);
        table.appendChild(thead);
        
        // Table body
        const tbody = document.createElement('tbody');
        
        // Add exercise rows
        exercises.forEach(exercise => {
            const row = document.createElement('tr');
            
            // Exercise name
            const nameCell = document.createElement('td');
            nameCell.textContent = exercise.name;
            row.appendChild(nameCell);
            
            // Add cells based on columns
            if (columns.includes('Sets')) {
                const cell = document.createElement('td');
                cell.textContent = exercise.sets || '-';
                row.appendChild(cell);
            }
            
            if (columns.includes('Reps')) {
                const cell = document.createElement('td');
                cell.textContent = exercise.reps || '-';
                row.appendChild(cell);
            }
            
            if (columns.includes('Duration')) {
                const cell = document.createElement('td');
                cell.textContent = exercise.duration || '-';
                row.appendChild(cell);
            }
            
            if (columns.includes('Rest')) {
                const cell = document.createElement('td');
                cell.textContent = exercise.rest || '-';
                row.appendChild(cell);
            }
            
            if (columns.includes('Tempo')) {
                const cell = document.createElement('td');
                cell.textContent = exercise.tempo || '-';
                row.appendChild(cell);
            }
            
            if (columns.includes('Time')) {
                const cell = document.createElement('td');
                cell.textContent = exercise.time || '-';
                row.appendChild(cell);
            }
            
            if (columns.includes('Rounds')) {
                const cell = document.createElement('td');
                cell.textContent = exercise.rounds || '-';
                row.appendChild(cell);
            }
            
            tbody.appendChild(row);
        });
        
        table.appendChild(tbody);
        sectionDiv.appendChild(table);
        
        return sectionDiv;
    }
    
    /**
     * Format goal string to be more readable
     * @param {string} goal - The goal string from the API
     * @returns {string} Formatted goal string
     */
    function formatGoal(goal) {
        switch (goal) {
            case 'muscle_gain':
                return 'Muscle Gain';
            case 'weight_loss':
                return 'Weight Loss';
            case 'strength':
                return 'Strength';
            case 'endurance':
                return 'Endurance';
            default:
                return capitalizeFirstLetter(goal);
        }
    }
    
    /**
     * Capitalize the first letter of a string
     * @param {string} str - Input string
     * @returns {string} String with first letter capitalized
     */
    function capitalizeFirstLetter(str) {
        return str.charAt(0).toUpperCase() + str.slice(1);
    }
});
