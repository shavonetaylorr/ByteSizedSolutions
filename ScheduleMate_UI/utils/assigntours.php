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

// Fetch roles for a specific tour type
function getRolesForTourType($conn, $tour_type) {
    $stmt = $conn->prepare("SELECT role_id, role_name FROM Roles WHERE tour_type = ?");
    $stmt->bind_param("s", $tour_type);
    $stmt->execute();
    $result = $stmt->get_result();
    return $result->fetch_all(MYSQLI_ASSOC);
}

// Fetch eligible ambassadors based on availability and workload
function getAvailableAmbassadors($conn, $weekday, $start_time, $end_time) {
    $query = "
        SELECT A.StuID, A.experienced, COUNT(Assign.assignment_id) AS workload
        FROM Availability Av
        JOIN Ambassadors A ON Av.StuID = A.StuID
        LEFT JOIN Assignments Assign ON A.StuID = Assign.StuID
        WHERE Av.weekday = ? AND Av.start_time <= ? AND Av.end_time >= ?
        GROUP BY A.StuID
        ORDER BY A.experienced DESC, workload ASC";
    
    $stmt = $conn->prepare($query);
    $stmt->bind_param("sss", $weekday, $start_time, $end_time);
    $stmt->execute();
    $result = $stmt->get_result();
    return $result->fetch_all(MYSQLI_ASSOC);
}

// Assign worker to a specific tour and role
function assignWorkerToTour($conn, $tour_id, $StuID, $role_id) {
    $stmt = $conn->prepare("SELECT * FROM Assignments WHERE tour_id = ? AND StuID = ? AND role_id = ?");
    $stmt->bind_param("iii", $tour_id, $StuID, $role_id);
    $stmt->execute();
    $existing_assignment = $stmt->get_result()->fetch_assoc();

    if ($existing_assignment) {
        return "Ambassador $StuID is already assigned to tour $tour_id for role $role_id.";
    } else {
        $stmt = $conn->prepare("INSERT INTO Assignments (tour_id, StuID, role_id) VALUES (?, ?, ?)");
        $stmt->bind_param("iii", $tour_id, $StuID, $role_id);
        $stmt->execute();
        return "Assigned Ambassador $StuID to role $role_id for tour $tour_id.";
    }
}

// Fetch all tours and process assignments
function assignTours() {
    $conn = dbConnection();

    $query = "SELECT * FROM Tours";
    $tours_result = $conn->query($query);

    $response = [];

    while ($tour = $tours_result->fetch_assoc()) {
        $tour_id = $tour['tour_id'];
        $tour_type = $tour['tour_type'];
        $weekday = $tour['weekday'];
        $start_time = $tour['start_time'];
        $end_time = $tour['end_time'];

        // Fetch roles for the tour type
        $roles = getRolesForTourType($conn, $tour_type);

        // Fetch eligible ambassadors
        $ambassadors = getAvailableAmbassadors($conn, $weekday, $start_time, $end_time);

        foreach ($roles as $role) {
            if (!empty($ambassadors)) {
                $ambassador = array_shift($ambassadors);
                $response[] = assignWorkerToTour($conn, $tour_id, $ambassador['StuID'], $role['role_id']);
            } else {
                $response[] = "No ambassadors available for role {$role['role_name']} in tour $tour_id.";
            }
        }
    }

    $conn->close();
    return $response;
}

// Handle API requests
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    $result = assignTours();
    header('Content-Type: application/json');
    echo json_encode($result);
}
?>
