// Fetch assignments dynamically
function fetchAssignments() {
    fetch('assign_tours.php')
        .then(response => response.json())
        .then(data => {
            console.log("Assignments:", data);
            // Update the frontend dynamically
            const resultContainer = document.getElementById('result-container');
            resultContainer.innerHTML = data.map(item => `<p>${item}</p>`).join('');
        })
        .catch(error => console.error("Error:", error));
}

// Trigger the fetch function
document.getElementById('fetch-assignments-btn').addEventListener('click', fetchAssignments);
