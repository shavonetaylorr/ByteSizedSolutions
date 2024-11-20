from enum import Enum # for days of the week
from collections import defaultdict

class DayOfWeek(Enum):
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'

class ScheduleManager:
    def __init__(self):
        self._schedule = defaultdict(list)
        self.initialize_fixed_tours()

    # Initialize with fixed tour days and types
    def initialize_fixed_tours(self):
        # Example fixed schedule: Mondays for Info Sessions, Tuesdays for Group Tours
        self._schedule[DayOfWeek.MONDAY] = ["KIST"]
        self._schedule[DayOfWeek.TUESDAY] = ["Group Tour"]
        self._schedule[DayOfWeek.THURSDAY] = ["KIST"]

    # Display the current schedule
    def display_schedule(self):
        print("Weekly Tour Schedule:")
        for day, tours in self._schedule.items():
            print(f"{day.value}: {', '.join(tours)}")

    # Add a new tour type to a specific day
    def add_tour(self, day, tour_type):
        self._schedule[day].append(tour_type)
        print(f"{tour_type} added on {day.value}.")

    # Remove a tour type from a specific day
    def remove_tour(self, day, tour_type):
        if tour_type in self._schedule[day]:
            self._schedule[day].remove(tour_type)
            print(f"{tour_type} removed from {day.value}.")
        else:
            print(f"{tour_type} not found on {day.value}.")
# Example usage
if __name__ == "__main__":
    manager = ScheduleManager()
    manager.display_schedule()

    # Example: Adding and removing tours
    manager.add_tour(DayOfWeek.WEDNESDAY, "VIP Tour")
    manager.remove_tour(DayOfWeek.MONDAY, "KIST")

    manager.display_schedule()
