#1.4 As a manager, I want to ensure each ambassador doesn’t 
# exceed 3 tours so that the work is divided evenly.

from collections import defaultdict
from datetime import datetime


class TourManager:
    def __init__(self):
        # Tracks the number of tours assigned per ambassador per month
        self.ambassador_tour_count = defaultdict(lambda: defaultdict(int))
        self.tours = []  # Keeps a record of all scheduled tours

    def add_ambassador(self, ambassador_name):
        """Adds a new ambassador."""
        if ambassador_name not in self.ambassador_tour_count:
            self.ambassador_tour_count[ambassador_name]  # Initialize the ambassador
            print(f"Ambassador {ambassador_name} added.")
        else:
            print(f"Ambassador {ambassador_name} already exists.")

    def assign_tour(self, ambassador_name, tour_name, tour_type, tour_date):
        """
        Assigns a tour to an ambassador if they haven't exceeded the limit of 3 tours per month.
        """
        if ambassador_name not in self.ambassador_tour_count:
            print(f"Ambassador {ambassador_name} does not exist. Add them first.")
            return

        month_key = (tour_date.year, tour_date.month)  # Use (year, month) to track tours by month for 2024

        if self.ambassador_tour_count[ambassador_name][month_key] < 3:
            self.ambassador_tour_count[ambassador_name][month_key] += 1
            self.tours.append({
                "ambassador": ambassador_name,
                "tour_name": tour_name,
                "tour_type": tour_type,
                "date": tour_date
            })
            print(f"Tour '{tour_name}' ({tour_type}) assigned to Ambassador {ambassador_name} on {tour_date}.")
        else:
            print(f"Ambassador {ambassador_name} already has 3 tours assigned for {tour_date.strftime('%B %Y')}. Cannot assign more.")

    def view_ambassador_tours(self, ambassador_name):
        """Displays all tours assigned to a specific ambassador."""
        assigned_tours = [tour for tour in self.tours if tour["ambassador"] == ambassador_name]
        if not assigned_tours:
            print(f"No tours assigned to {ambassador_name}.")
        else:
            print(f"Tours assigned to {ambassador_name}:")
            for tour in assigned_tours:
                print(f"- {tour['tour_name']} ({tour['tour_type']}) on {tour['date']}")

    def view_all_assignments(self):
        """Displays all tour assignments."""
        if not self.tours:
            print("No tours assigned yet.")
        else:
            print("All Tour Assignments:")
            for tour in self.tours:
                print(f"- {tour['tour_name']} ({tour['tour_type']}) on {tour['date']} assigned to {tour['ambassador']}")



if __name__ == "__main__":
    manager = TourManager()

    # Add ambassadors
    manager.add_ambassador("Joe")
    manager.add_ambassador("Delaia")

    # Assign the different tour types 
    manager.assign_tour("Joe", "Group Tour 1", "Group", datetime(2024, 11, 5, 10))
    manager.assign_tour("Joe", "KIST Tour 1", "KIST", datetime(2024, 11, 12))
    manager.assign_tour("Joe", "Private Tour 1", "Private", datetime(2024, 11, 20, 3))
    manager.assign_tour("Joe", "Group Tour 2", "Group", datetime(2024, 11, 25, 12))  # Should fail (limit exceeded)

    manager.assign_tour("Delaia", "KIST Tour 2", "KIST", datetime(2024, 11, 5, 10))
    manager.assign_tour("Delaia", "Private Tour 2", "Private", datetime(2024, 11, 12, 12))
    manager.assign_tour("Delaia", "Group Tour 3", "Group", datetime(2024, 11, 20, 2))
    manager.assign_tour("Delaia", "KIST Tour 3", "KIST", datetime(2024, 11, 25, 10))  # Should fail (limit exceeded)

    # View assignments
    manager.view_ambassador_tours("Joe")
    manager.view_all_assignments()
