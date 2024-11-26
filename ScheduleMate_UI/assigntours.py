import pymysql
from dbconfig import db_config


def get_roles_for_tour_type(cursor, tour_type):
    """
    Fetch roles required for a specific tour type.
    """
    cursor.execute("""
        SELECT role_id, role_name
        FROM Roles
        WHERE tour_type = %s
    """, (tour_type,))
    return cursor.fetchall()


def get_available_ambassadors(cursor, tour_weekday, tour_start, tour_end):
    """
    Fetch eligible ambassadors based on availability and workload.
    """
    cursor.execute("""
        SELECT A.StuID, A.experienced, COUNT(Assign.assignment_id) AS workload
        FROM Availability Av
        JOIN Ambassadors A ON Av.StuID = A.StuID
        LEFT JOIN Assignments Assign ON A.StuID = Assign.StuID
        WHERE Av.weekday = %s
          AND Av.start_time <= %s
          AND Av.end_time >= %s
        GROUP BY A.StuID
        ORDER BY A.experienced DESC, workload ASC
    """, (tour_weekday, tour_start, tour_end))
    return cursor.fetchall()


def assign_worker_to_tour(cursor, tour_id, StuID, role_id):
    """
    Assign a worker to a specific tour and role, ensuring no duplicates.
    """
    cursor.execute("""
        SELECT * FROM Assignments
        WHERE tour_id = %s AND StuID = %s AND role_id = %s
    """, (tour_id, StuID, role_id))
    existing_assignment = cursor.fetchone()

    if existing_assignment:
        print(f"Ambassador {StuID} is already assigned to tour {tour_id} for role {role_id}.")
    else:
        cursor.execute("""
            INSERT INTO Assignments (tour_id, StuID, role_id)
            VALUES (%s, %s, %s)
        """, (tour_id, StuID, role_id))
        print(f"Assigned Ambassador {StuID} to role {role_id} for tour {tour_id}.")


def get_assigned_workers(cursor, tour_id):
    """
    Fetch assigned workers and their roles for a specific tour.
    """
    cursor.execute("""
        SELECT A.StuID, A.name, R.role_name
        FROM Assignments Assign
        JOIN Ambassadors A ON Assign.StuID = A.StuID
        JOIN Roles R ON Assign.role_id = R.role_id
        WHERE Assign.tour_id = %s
    """, (tour_id,))
    return cursor.fetchall()


def assign_tours():
    """
    Main function to assign workers to tours and roles.
    """
    connection = pymysql.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database'],
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Tours")
            tours = cursor.fetchall()

            for tour in tours:
                tour_id = tour['tour_id']
                tour_type = tour['tour_type']
                tour_weekday = tour['weekday']
                tour_start = tour['start_time']
                tour_end = tour['end_time']

                print(f"\nProcessing Tour ID: {tour_id} | Type: {tour_type} | {tour_weekday} | {tour_start} - {tour_end}")

                # Step 1: Get required roles directly from Roles table
                roles = get_roles_for_tour_type(cursor, tour_type)
                print(f"  Required Roles: {[role['role_name'] for role in roles]}")

                # Step 2: Get eligible ambassadors
                eligible_ambassadors = get_available_ambassadors(cursor, tour_weekday, tour_start, tour_end)
                if not eligible_ambassadors:
                    print(f"  No eligible ambassadors available for Tour {tour_id}.")
                    continue

                print(f"  Eligible Ambassadors: {[amb['StuID'] for amb in eligible_ambassadors]}")

                # Step 3: Assign roles
                for role in roles:
                    if eligible_ambassadors:
                        ambassador = eligible_ambassadors.pop(0)
                        assign_worker_to_tour(cursor, tour_id, ambassador['StuID'], role['role_id'])
                    else:
                        print(f"  No ambassadors available for role {role['role_name']} in Tour {tour_id}.")

                # Step 4: Display assigned workers
                assigned_workers = get_assigned_workers(cursor, tour_id)
                if assigned_workers:
                    print(f"  Assigned Workers for Tour {tour_id}:")
                    for worker in assigned_workers:
                        print(f"    Ambassador {worker['name']} (ID: {worker['StuID']}) as {worker['role_name']}")
                else:
                    print(f"  No workers assigned for Tour {tour_id}.")

            connection.commit()
    except Exception as e:
        print(f"Error: {e}")
        connection.rollback()
    finally:
        connection.close()


if __name__ == "__main__":
    assign_tours()
