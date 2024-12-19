<?php
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
// Fetch scheduled tours
function fetchScheduledTours() {
    $conn = dbConnection();
    $query = "SELECT * FROM Tours"; // Add filters or JOINs as needed
    $result = $conn->query($query);

    if ($result) {
        $tours = $result->fetch_all(MYSQLI_ASSOC);
        echo json_encode($tours);
    } else {
        echo json_encode(["error" => $conn->error]);
    }

    $conn->close();
}

// Handle request
header('Content-Type: application/json');
fetchScheduledTours();
