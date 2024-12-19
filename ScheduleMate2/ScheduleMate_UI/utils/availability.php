<?php
// Include database configuration
include 'dbconfig.php';

// Establish a database connection
function dbConnection() {
    global $hostname, $username, $password, $dbname;
    $conn = new mysqli($hostname, $username, $password, $dbname);

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    return $conn;
}

// Fetch ambassador availability, grouped by ambassador
function getAmbassadorAvailability($conn) {
    $query = "
        SELECT A.StuID, A.name AS ambassador_name, Av.weekday, Av.start_time, Av.end_time
        FROM Availability Av
        JOIN Ambassadors A ON Av.StuID = A.StuID
        ORDER BY A.name, 
                 FIELD(Av.weekday, 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'), 
                 Av.start_time;
    ";

    $result = $conn->query($query);
    if (!$result) {
        die("Error executing query: " . $conn->error);
    }

    $availabilityData = [];

    // Process each row and group availability by ambassador
    while ($row = $result->fetch_assoc()) {
        $StuID = $row['StuID'];
        if (!isset($availabilityData[$StuID])) {
            $availabilityData[$StuID] = [
                'ambassador_name' => $row['ambassador_name'],
                'availability' => []
            ];
        }

        $availabilityData[$StuID]['availability'][] = [
            'weekday' => $row['weekday'],
            'start_time' => $row['start_time'],
            'end_time' => $row['end_time']
        ];
    }

    return array_values($availabilityData); // Reset array keys for clean JSON output
}

// Handle GET request and return JSON response
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    $conn = dbConnection(); // Connect to the database

    // Get ambassador availability data
    $availabilityData = getAmbassadorAvailability($conn);

    $conn->close(); // Close the database connection

    // Return JSON-encoded response
    header('Content-Type: application/json');
    echo json_encode($availabilityData);
    exit();
}
