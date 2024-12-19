<?php
// Include database configuration
include '../utils/dbconfig.php';

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

// Fetch ambassador assignments for a specific tour
function getAmbassadorAssignments($conn, $tour_id) {
    $query = "
        SELECT 
            A.StuID, 
            A.name AS ambassador_name, 
            A.experienced, 
            R.role_name
        FROM Assignments T
        JOIN Ambassadors A ON T.StuID = A.StuID
        JOIN Roles R ON T.role_id = R.role_id
        WHERE T.tour_id = ?
    ";

    $stmt = $conn->prepare($query);
    if (!$stmt) {
        die("Error preparing statement: " . $conn->error);
    }

    $stmt->bind_param("i", $tour_id);
    $stmt->execute();

    $result = $stmt->get_result();
    $assignments = [];
    while ($row = $result->fetch_assoc()) {
        $assignments[] = [
            "StuID" => $row["StuID"],
            "name" => $row["ambassador_name"],
            "experienced" => $row["experienced"] == 1, // Convert to boolean
            "role_name" => $row["role_name"]
        ];
    }

    $stmt->close();
    return $assignments;
}


// Handle GET request
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    if (isset($_GET['tour_id']) && is_numeric($_GET['tour_id'])) {
        $tour_id = intval($_GET['tour_id']); // Sanitize and cast to integer
        $conn = dbConnection();

        $assignments = getAmbassadorAssignments($conn, $tour_id);
        $conn->close();

        header('Content-Type: application/json');
        echo json_encode($assignments);
    } else {
        header('Content-Type: application/json');
        echo json_encode(['error' => 'Tour ID not provided']);
    }
    exit();
}
