from utils.db_connection import db_connection  # Reuse DB connection setup
# User story 1.6: As a student ambassador, I want to see a breakdown of all scheduled tours, so that I can plan accordingly. 
def get_assigned_tours_for_ambassador(cursor, StuID):
    """
    Fetch all assigned tours for a specific ambassador.
    """
    cursor.execute("""
        SELECT T.tour_id, T.tour_type, T.weekday, T.start_time, T.end_time, R.role_name
        FROM Assignments A
        JOIN Tours T ON A.tour_id = T.tour_id
        JOIN Roles R ON A.role_id = R.role_id
        WHERE A.StuID = %s
        ORDER BY T.weekday, T.start_time
    """, (StuID,))
    return cursor.fetchall()

def list_all_tours_grouped_by_type(cursor):
    """
    List all tours, grouped by tour type (Group, KIST, Private).
    """
    cursor.execute("""
        SELECT tour_type, tour_id, weekday, start_time, end_time
        FROM Tours
        ORDER BY tour_type, weekday, start_time
    """)
    tours = cursor.fetchall()

    grouped_tours = {}
    for tour in tours:
        tour_type = tour['tour_type']
        if tour_type not in grouped_tours:
            grouped_tours[tour_type] = []
        grouped_tours[tour_type].append(tour)
    return grouped_tours


def view_ambassador_tours():
    """
    Display all tours assigned to a specific ambassador.
    """
    connection = db_connection()  # Use shared DB connection
    try:
        StuID = int(input("Enter Ambassador StuID to view their tours: "))
        with connection.cursor() as cursor:
            list_all_tours_grouped_by_type(cursor)
            tours = get_assigned_tours_for_ambassador(cursor, StuID)
            if not tours:
                print(f"No tours assigned to Ambassador ID: {StuID}.")
                return

            print(f"Tours assigned to Ambassador ID {StuID}:")
            for tour in tours:
                print(f"- Tour ID: {tour['tour_id']}, Type: {tour['tour_type']}, "
                      f"Day: {tour['weekday']}, Time: {tour['start_time']} - {tour['end_time']}, "
                      f"Role: {tour['role_name']}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()

if __name__ == "__main__":
    view_ambassador_tours()
