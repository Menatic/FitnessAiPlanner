/**
 * Fitness Plan Pro - Client-side JavaScript
 * Handles form submission, UI interactions, and displaying workout plans
 */

document.addEventListener('DOMContentLoaded', function() {
    // Main elements
    const workoutForm = document.getElementById('workoutForm');
    const loadingSpinner = document.getElementById('loadingSpinner');
    const errorAlert = document.getElementById('errorAlert');
    const errorMessage = document.getElementById('errorMessage');
    
    // Popup elements
    const workoutPopupOverlay = document.getElementById('workoutPopupOverlay');
    const workoutPopup = document.getElementById('workoutPopup');
    const popupWorkoutResult = document.getElementById('popupWorkoutResult');
    const closePopupBtn = document.getElementById('closePopup');
    
    // Equipment options with icons
    const equipmentOptions = [
        { id: 'dumbbells', name: 'Dumbbells', icon: 'bi-gear-fill' },
        { id: 'bench', name: 'Bench', icon: 'bi-dash-square-fill' },
        { id: 'resistance_band', name: 'Resistance Band', icon: 'bi-slash-circle-fill' },
        { id: 'barbell', name: 'Barbell', icon: 'bi-dash-lg' },
        { id: 'kettlebell', name: 'Kettlebell', icon: 'bi-record-circle-fill' },
        { id: 'medicine_ball', name: 'Medicine Ball', icon: 'bi-circle-fill' },
        { id: 'pull_up_bar', name: 'Pull-up Bar', icon: 'bi-dash-lg' }
    ];
    
    // Populate equipment checkboxes with nicer styling
    const equipmentContainer = document.getElementById('equipmentContainer');
    if (equipmentContainer) {
        // Create a row for equipment items
        const row = document.createElement('div');
        row.className = 'row';
        
        equipmentOptions.forEach(equipment => {
            // Create a column for each equipment
            const col = document.createElement('div');
            col.className = 'col-md-6 equipment-item';
            
            const div = document.createElement('div');
            div.className = 'form-check';
            
            const input = document.createElement('input');
            input.className = 'form-check-input';
            input.type = 'checkbox';
            input.id = `equipment_${equipment.id}`;
            input.name = 'equipment';
            input.value = equipment.id;
            
            const label = document.createElement('label');
            label.className = 'form-check-label';
            label.htmlFor = `equipment_${equipment.id}`;
            label.innerHTML = `<i class="bi ${equipment.icon} me-2"></i>${equipment.name}`;
            
            div.appendChild(input);
            div.appendChild(label);
            col.appendChild(div);
            row.appendChild(col);
        });
        
        equipmentContainer.appendChild(row);
    }
    
    // Toggle popup visibility
    function togglePopup(show = true) {
        if (show) {
            document.body.style.overflow = 'hidden'; // Prevent scrolling behind popup
            workoutPopupOverlay.classList.add('active');
            setTimeout(() => {
                workoutPopup.classList.add('active');
            }, 50); // Small delay for animation
        } else {
            workoutPopup.classList.remove('active');
            setTimeout(() => {
                workoutPopupOverlay.classList.remove('active');
                document.body.style.overflow = '';
            }, 300); // Wait for animation to complete
        }
    }
    
    // Close popup when clicking the close button
    if (closePopupBtn) {
        closePopupBtn.addEventListener('click', function() {
            togglePopup(false);
        });
    }
    
    // Close popup when clicking outside the popup content
    if (workoutPopupOverlay) {
        workoutPopupOverlay.addEventListener('click', function(event) {
            if (event.target === workoutPopupOverlay) {
                togglePopup(false);
            }
        });
        
        // Also close on escape key
        document.addEventListener('keydown', function(event) {
            if (event.key === 'Escape' && workoutPopupOverlay.classList.contains('active')) {
                togglePopup(false);
            }
        });
    }
    
    // Handle form submission
    if (workoutForm) {
        workoutForm.addEventListener('submit', function(event) {
            event.preventDefault();
            
            // Show loading spinner and hide previous errors
            loadingSpinner.classList.remove('d-none');
            errorAlert.classList.add('d-none');
            
            // Get form data
            const formData = new FormData(workoutForm);
            
            // Validate that at least one equipment is selected
            const equipment = Array.from(formData.getAll('equipment'));
            if (equipment.length === 0) {
                loadingSpinner.classList.add('d-none');
                errorMessage.textContent = "Please select at least one piece of equipment";
                errorAlert.classList.remove('d-none');
                return;
            }
            
            // Create request payload
            const payload = {
                name: formData.get('name'),
                age: parseInt(formData.get('age')),
                gender: formData.get('gender'),
                goal: formData.get('goal'),
                experience: formData.get('experience'),
                equipment: equipment,
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
                        throw new Error(data.error || 'An error occurred while generating your workout plan');
                    });
                }
                return response.json();
            })
            .then(data => {
                // Display the results in the popup
                displayWorkoutPlanInPopup(data);
                // Hide loading spinner and show popup
                loadingSpinner.classList.add('d-none');
                togglePopup(true);
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
     * Display the workout plan in the popup
     * @param {Object} workoutPlan - The workout plan data from the API
     */
    function displayWorkoutPlanInPopup(workoutPlan) {
        // Clear previous results
        popupWorkoutResult.innerHTML = '';
        
        // Add print and export buttons
        const actionButtons = document.createElement('div');
        actionButtons.className = 'd-flex justify-content-end mb-4';
        
        const printBtn = document.createElement('button');
        printBtn.className = 'btn btn-success me-2';
        printBtn.innerHTML = '<i class="bi bi-printer me-2"></i>Print Workout';
        printBtn.onclick = function() { window.print(); };
        
        const exportBtn = document.createElement('button');
        exportBtn.className = 'btn btn-info';
        exportBtn.innerHTML = '<i class="bi bi-download me-2"></i>Export Plan';
        exportBtn.onclick = function() {
            // Create a JSON file for download
            const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(workoutPlan, null, 2));
            const downloadAnchorNode = document.createElement('a');
            downloadAnchorNode.setAttribute("href", dataStr);
            downloadAnchorNode.setAttribute("download", `${workoutPlan.client_profile.name}_workout_plan.json`);
            document.body.appendChild(downloadAnchorNode);
            downloadAnchorNode.click();
            downloadAnchorNode.remove();
        };
        
        actionButtons.appendChild(printBtn);
        actionButtons.appendChild(exportBtn);
        popupWorkoutResult.appendChild(actionButtons);
        
        // Create client profile summary
        const profileSummary = document.createElement('div');
        profileSummary.className = 'card mb-4';
        profileSummary.innerHTML = `
            <div class="card-body">
                <div class="d-flex align-items-center mb-3">
                    <i class="bi bi-person-circle text-primary me-3" style="font-size: 2rem;"></i>
                    <div>
                        <h3 class="card-title mb-1">Workout Plan for ${workoutPlan.client_profile.name}</h3>
                        <p class="text-muted mb-0">12-Session Progressive Training Program</p>
                    </div>
                </div>
                <hr>
                <div class="row">
                    <div class="col-md-6">
                        <p><i class="bi bi-calendar3 me-2"></i><strong>Age:</strong> ${workoutPlan.client_profile.age}</p>
                        <p><i class="bi bi-gender-ambiguous me-2"></i><strong>Gender:</strong> ${capitalizeFirstLetter(workoutPlan.client_profile.gender)}</p>
                    </div>
                    <div class="col-md-6">
                        <p><i class="bi bi-bullseye me-2"></i><strong>Goal:</strong> ${formatGoal(workoutPlan.client_profile.goal)}</p>
                        <p><i class="bi bi-bar-chart-line me-2"></i><strong>Experience:</strong> ${capitalizeFirstLetter(workoutPlan.client_profile.experience)}</p>
                    </div>
                </div>
                <p><i class="bi bi-calendar-week me-2"></i><strong>Training Days:</strong> ${workoutPlan.client_profile.days_per_week} days per week</p>
                <p><i class="bi bi-gear-wide me-2"></i><strong>Equipment:</strong> ${workoutPlan.client_profile.equipment.map(e => formatEquipmentName(e)).join(', ')}</p>
            </div>
        `;
        popupWorkoutResult.appendChild(profileSummary);
        
        // Group sessions by week
        const sessionsByWeek = {};
        workoutPlan.sessions.forEach(session => {
            if (!sessionsByWeek[session.week]) {
                sessionsByWeek[session.week] = [];
            }
            sessionsByWeek[session.week].push(session);
        });
        
        // Create a card for each week
        Object.keys(sessionsByWeek).forEach(week => {
            const weekCard = document.createElement('div');
            weekCard.className = 'card mb-4';
            
            // Week header
            const weekHeader = document.createElement('div');
            weekHeader.className = 'card-header';
            weekHeader.innerHTML = `
                <div class="d-flex align-items-center">
                    <i class="bi bi-calendar-week me-2" style="font-size: 1.5rem;"></i>
                    <h3 class="mb-0">Week ${week}</h3>
                </div>
            `;
            weekCard.appendChild(weekHeader);
            
            // Week content
            const weekBody = document.createElement('div');
            weekBody.className = 'card-body';
            
            // Create a session accordion for this week
            const weekAccordion = document.createElement('div');
            weekAccordion.className = 'accordion';
            weekAccordion.id = `week${week}Accordion`;
            
            // Add each session to the accordion
            sessionsByWeek[week].forEach((session, index) => {
                const sessionId = `week${week}-session-${index}`;
                const sessionDiv = document.createElement('div');
                sessionDiv.className = `accordion-item workout-${session.workout_type}`;
                
                // Icon for workout type
                let workoutIcon = 'bi-activity';
                switch (session.workout_type) {
                    case 'push': workoutIcon = 'bi-arrow-up-circle'; break;
                    case 'pull': workoutIcon = 'bi-arrow-down-circle'; break;
                    case 'legs': workoutIcon = 'bi-arrow-down-square'; break;
                    case 'upper': workoutIcon = 'bi-arrow-up'; break;
                    case 'lower': workoutIcon = 'bi-arrow-down'; break;
                    case 'full_body': workoutIcon = 'bi-person'; break;
                }
                
                // Session header
                const sessionHeader = document.createElement('h2');
                sessionHeader.className = 'accordion-header';
                sessionHeader.id = `heading-${sessionId}`;
                
                const sessionButton = document.createElement('button');
                sessionButton.className = `accordion-button ${index > 0 ? 'collapsed' : ''}`;
                sessionButton.type = 'button';
                sessionButton.setAttribute('data-bs-toggle', 'collapse');
                sessionButton.setAttribute('data-bs-target', `#collapse-${sessionId}`);
                sessionButton.setAttribute('aria-expanded', index === 0 ? 'true' : 'false');
                sessionButton.setAttribute('aria-controls', `collapse-${sessionId}`);
                
                sessionButton.innerHTML = `
                    <div class="d-flex align-items-center w-100">
                        <div class="d-flex align-items-center">
                            <i class="bi ${workoutIcon} me-2" style="font-size: 1.25rem;"></i>
                            <span class="fw-bold">Session ${session.session}</span>
                        </div>
                        <div class="ms-auto d-flex align-items-center">
                            <span class="badge bg-primary me-2">${capitalizeFirstLetter(session.workout_type)} Day</span>
                            <span class="text-muted small">${session.date}</span>
                        </div>
                    </div>
                `;
                
                sessionHeader.appendChild(sessionButton);
                sessionDiv.appendChild(sessionHeader);
                
                // Session content
                const sessionContent = document.createElement('div');
                sessionContent.id = `collapse-${sessionId}`;
                sessionContent.className = `accordion-collapse collapse ${index === 0 ? 'show' : ''}`;
                sessionContent.setAttribute('aria-labelledby', `heading-${sessionId}`);
                sessionContent.setAttribute('data-bs-parent', `#week${week}Accordion`);
                
                const sessionBody = document.createElement('div');
                sessionBody.className = 'accordion-body';
                
                // Icons for each section
                const sectionIcons = {
                    'Warm-up': 'bi-thermometer-sun',
                    'Main Exercises': 'bi-award',
                    'Circuit': 'bi-lightning-charge',
                    'Superset': 'bi-stopwatch',
                    'Cool-down': 'bi-snow'
                };
                
                // Create sections
                if (session.sections.warmup && session.sections.warmup.length > 0) {
                    sessionBody.appendChild(
                        createEnhancedSectionElement('Warm-up', session.sections.warmup, sectionIcons['Warm-up'])
                    );
                }
                
                if (session.sections.main && session.sections.main.length > 0) {
                    sessionBody.appendChild(
                        createEnhancedSectionElement('Main Exercises', session.sections.main, sectionIcons['Main Exercises'])
                    );
                }
                
                if (session.sections.circuit && session.sections.circuit.length > 0) {
                    sessionBody.appendChild(
                        createEnhancedSectionElement('Circuit', session.sections.circuit, sectionIcons['Circuit'])
                    );
                }
                
                if (session.sections.superset && session.sections.superset.length > 0) {
                    sessionBody.appendChild(
                        createEnhancedSectionElement('Superset', session.sections.superset, sectionIcons['Superset'])
                    );
                }
                
                if (session.sections.cooldown && session.sections.cooldown.length > 0) {
                    sessionBody.appendChild(
                        createEnhancedSectionElement('Cool-down', session.sections.cooldown, sectionIcons['Cool-down'])
                    );
                }
                
                sessionContent.appendChild(sessionBody);
                sessionDiv.appendChild(sessionContent);
                weekAccordion.appendChild(sessionDiv);
            });
            
            weekBody.appendChild(weekAccordion);
            weekCard.appendChild(weekBody);
            popupWorkoutResult.appendChild(weekCard);
        });
        
        // Add a note about progressive overload
        const noteDiv = document.createElement('div');
        noteDiv.className = 'alert alert-info';
        noteDiv.innerHTML = `
            <div class="d-flex align-items-start">
                <i class="bi bi-info-circle-fill me-3 mt-1" style="font-size: 1.5rem;"></i>
                <div>
                    <h5 class="alert-heading">Progressive Overload</h5>
                    <p class="mb-0">This workout plan incorporates progressive overload principles - the exercises get increasingly challenging over the 4 weeks through adjustments in sets, reps, and rest periods. Follow the plan in order for best results.</p>
                </div>
            </div>
        `;
        popupWorkoutResult.appendChild(noteDiv);
    }
    
    /**
     * Create an enhanced section element for a workout section with better styling
     */
    function createEnhancedSectionElement(title, exercises, icon) {
        const sectionDiv = document.createElement('div');
        sectionDiv.className = 'mb-4';
        
        // Section title with icon
        const sectionTitle = document.createElement('h4');
        sectionTitle.className = 'section-title';
        sectionTitle.innerHTML = `<i class="bi ${icon} me-2"></i>${title}`;
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
            
            // Exercise name cell with animation
            const nameCell = document.createElement('td');
            nameCell.innerHTML = `<strong>${exercise.name}</strong>`;
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
     * Format equipment name to be more readable
     */
    function formatEquipmentName(equipment) {
        return equipment
            .split('_')
            .map(word => word.charAt(0).toUpperCase() + word.slice(1))
            .join(' ');
    }
    
    /**
     * Format goal string to be more readable
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
     */
    function capitalizeFirstLetter(str) {
        return str.charAt(0).toUpperCase() + str.slice(1);
    }
});
