-- Create the Tours table to store predefined tour schedules
CREATE TABLE Tours (
    tour_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tour, auto-incremented
    tour_type VARCHAR(50) NOT NULL,         -- Type of tour (e.g., Private, Group, KIST)
    weekday ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') NOT NULL,     -- Day of the week the tour is scheduled
    start_time TIME NOT NULL,               -- Start time of the tour
    end_time TIME NOT NULL                  -- End time of the tour
);
-- Add an index to optimize queries filtering or joining on weekday and start_time
CREATE INDEX idx_tours_weekday_start ON Tours (weekday, start_time);

-- Create the Ambassadors table to store information about student ambassadors
CREATE TABLE Ambassadors (
    StuID INT PRIMARY KEY,               -- Unique student ID, serves as the primary key
    name VARCHAR(100) NOT NULL,          -- Ambassador's name, up to 100 characters
    phone_number VARCHAR(15) NOT NULL,   -- Contact number, formatted as a string
    experienced BOOLEAN NOT NULL         -- Indicates if the ambassador is experienced (1 for true, 0 for false)
);

-- Create the Availability table to link student ambassadors with their availability time slots
CREATE TABLE Availability (
    StuID INT NOT NULL,                  -- Student ID linking to the Ambassadors table
    weekday ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') NOT NULL,        -- Day of the week for the availability
    start_time TIME NOT NULL,            -- Availability start time
    end_time TIME NOT NULL,              -- Availability end time
    PRIMARY KEY (StuID, weekday, start_time), -- Composite primary key to ensure unique time slots for each student
    FOREIGN KEY (StuID) REFERENCES Ambassadors(StuID) ON DELETE CASCADE -- Foreign key enforces referential integrity, cascading deletions if a student is removed from the Ambassadors table.
);
-- Add an index to optimize queries filtering or joining on weekday and start_time
CREATE INDEX idx_availability_weekday_start ON Availability (weekday, start_time);

-- Aleardy Ran below code
-- ALTER TABLE Availability
-- ADD month VARCHAR(20) NOT NULL DEFAULT 'Unknown';


-- Create the Roles table to define roles for each tour type
CREATE TABLE Roles (
    role_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each role
    tour_type ENUM('KIST', 'Private', 'Group') NOT NULL,  -- Type of tour (e.g., KIST, Private, Group)
    role_name VARCHAR(50) NOT NULL,          -- Role within the tour (e.g., Speaker, Tour Guide)
	UNIQUE (tour_type, role_name)            -- Ensures no duplicate role names for the same tour type
);

-- Insert example roles
INSERT INTO Roles (tour_type, role_name)
VALUES
    ('KIST', 'Speaker'),
    ('KIST', 'Setup/Check-in'),
    ('KIST', 'Tour Guide'),
    ('Private', 'Tour Guide'),
    ('Group', 'Tour Guide');
    

-- Create the Assignments table to track which ambassador is assigned to which tour
CREATE TABLE Assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique assignment ID, auto-incremented
    tour_id INT NOT NULL,                         -- Foreign key linking to the Tours table
    StuID INT NOT NULL,                           -- Foreign key linking to the Ambassadors table
    role_id INT NOT NULL,                         -- Foreign key linking to the Roles table
    FOREIGN KEY (tour_id) REFERENCES Tours(tour_id) ON DELETE CASCADE, -- Ensures referential integrity with the Tours table
    FOREIGN KEY (StuID) REFERENCES Ambassadors(StuID) ON DELETE CASCADE, -- Ensures referential integrity with the Ambassadors table
	FOREIGN KEY (role_id) REFERENCES Roles(role_id) ON DELETE CASCADE
);

CREATE TABLE Assigned_Ambassadors (
    AAid INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each assignment
    tour_id INT NOT NULL,                        -- Foreign key linking to Tours
    StuID INT NOT NULL,                          -- Foreign key linking to Ambassadors
    assigned_date DATE NOT NULL,                 -- Date of assignment (e.g., Week or Day)
    -- assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Automatically stores the timestamp of assignment
    FOREIGN KEY (tour_id) REFERENCES Tours(tour_id) ON DELETE CASCADE,
    FOREIGN KEY (StuID) REFERENCES Ambassadors(StuID) ON DELETE CASCADE,
    UNIQUE (tour_id, StuID, assigned_date)       -- Prevents duplicate assignments for the same tour, ambassador, and date
);

