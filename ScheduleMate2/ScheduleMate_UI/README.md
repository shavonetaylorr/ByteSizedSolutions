# ScheduleMate
A web-based scheduling system designed to automate tour management for the Office of Admissions, simplifying staff coordination and improving scheduling efficiency.
## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Technologies Used](#technologies-used)
6. [Contributors](#contributors)
7. [License](#license)
## Introduction
ScheduleMate is a scheduling solution designed to manage tours and ambassador assignments efficiently. It allows administrators to track availability, assign roles, *send notifications, and manage schedules via an intuitive interface.
## Features
- **Automated Scheduling**: Assign ambassadors based on availability and workload.
- **View Schedules**: View the schedules of all ambassadors.
- **Shift Swapping**: Ambassadors can swap shifts in real-time (future enhancement).
- **Notifications**: Automated SMS reminders via Twilio (future enhancement).
- **Data Visualization**: Graphs showing tour statistics (future enhancement).
- **User-Friendly Interface**: Simplified navigation for managers and ambassadors.

## Installation
Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/username/ScheduleMate.git

cd ScheduleMate

2. Set up the database:

Import the schedulemate.sql file into your MySQL database.
Update database credentials in utils/dbconfig.php.
Start a local server using XAMPP or a similar tool.

Access the project:

Open http://localhost/ScheduleMate_UI in your browser.


---

#### **6. Usage**
```markdown
## Usage
1. Log in as a manager or ambassador.
2. Managers can:
   - View and manage schedules.
   - Assign roles for tours.
   - Notify ambassadors about upcoming events.
3. Ambassadors can:
   - Check their schedules.
   - Swap shifts with peers.
4. Access the system dashboard to manage tours and notifications.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: PHP, MySQL
- **Frameworks/Tools**:
  - Twilio (for SMS notifications) (future enhancement)
  - XAMPP (local server testing)
  - GitHub (version control)

## Contributors

| Name | Email |
|------|--------|
| Kim | 
| Ishan |
| Essence |
| Shavone |
| Janai |



## License
This project is licensed under the MIT License. See `LICENSE` for more details.
