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

// Fetch available ambassadors for a tour
function getAvailableAmbassadors($conn, $tour_id) {
    // Query to fetch the tour details (weekday, start_time, end_time)
    $tourQuery = "
        SELECT weekday, start_time, end_time 
        FROM Tours 
        WHERE tour_id = ?;
    ";
    $stmt = $conn->prepare($tourQuery);
    $stmt->bind_param("i", $tour_id);
    $stmt->execute();
    $tourResult = $stmt->get_result();

    if ($tourResult->num_rows === 0) {
        return ["error" => "Tour not found"];
    }

    $tour = $tourResult->fetch_assoc();
    $weekday = $tour['weekday'];
    $start_time = $tour['start_time'];
    $end_time = $tour['end_time'];

    // Query to fetch ambassadors not assigned to the given tour and available during the tour time
    $availableAmbassadorsQuery = "
        SELECT A.StuID, A.name, A.experienced 
        FROM Ambassadors A
        LEFT JOIN Assignments Asgn ON A.StuID = Asgn.StuID AND Asgn.tour_id = ?
        INNER JOIN Availability Av ON A.StuID = Av.StuID
        WHERE Asgn.assignment_id IS NULL
          AND Av.weekday = ?
          AND Av.start_time <= ?
          AND Av.end_time >= ?
        ORDER BY A.name;
    ";
    $stmt = $conn->prepare($availableAmbassadorsQuery);
    $stmt->bind_param("isss", $tour_id, $weekday, $start_time, $end_time);
    $stmt->execute();
    $result = $stmt->get_result();

    $availableAmbassadors = [];
    while ($row = $result->fetch_assoc()) {
        $availableAmbassadors[] = $row;
    }

    return $availableAmbassadors;
}

// Handle GET request
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    if (!isset($_GET['tour_id'])) {
        echo json_encode(["error" => "Tour ID not provided"]);
        exit();
    }

    $tour_id = intval($_GET['tour_id']);
    $conn = dbConnection(); // Connect to the database

    $availableAmbassadors = getAvailableAmbassadors($conn, $tour_id);

    $conn->close(); // Close the database connection

    // Return JSON-encoded response
    header('Content-Type: application/json');
    echo json_encode($availableAmbassadors);
    exit();
}
?>
