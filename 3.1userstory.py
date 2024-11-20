from abc import ABC, abstractmethod
from datetime import date, datetime, timedelta


# Step 1: Define a base class for common tour properties.
class ITour(ABC):
    def __init__(self, tour_name, start_date, end_date, location, start_time, end_time):
        self.tour_name = tour_name
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.start_time = start_time
        self.end_time = end_time

    @abstractmethod
    def schedule_tour(self):
        pass


# Step 2: Create specific classes for each tour type.
class GroupTour(ITour):
    def __init__(self, tour_name, start_date, end_date, location, start_time, end_time):
        super().__init__(tour_name, start_date, end_date, location, start_time, end_time)
        self.tour_type = "Group"

    def schedule_tour(self):
        print(f"Group Tour '{self.tour_name}' scheduled from {self.start_date} to {self.end_date} "
              f"at {self.location} from {self.start_time} to {self.end_time}.")


class KISTTour(ITour):
    def __init__(self, tour_name, start_date, end_date, location, start_time, end_time):
        super().__init__(tour_name, start_date, end_date, location, start_time, end_time)
        self.tour_type = "KIST"

    def schedule_tour(self):
        print(f"KIST Tour '{self.tour_name}' scheduled from {self.start_date} to {self.end_date} "
              f"at {self.location} from {self.start_time} to {self.end_time}.")


class PrivateTour(ITour):
    def __init__(self, tour_name, start_date, end_date, location, start_time, end_time):
        super().__init__(tour_name, start_date, end_date, location, start_time, end_time)
        self.tour_type = "Private"

    def schedule_tour(self):
        print(f"Private Tour '{self.tour_name}' scheduled from {self.start_date} to {self.end_date} "
              f"at {self.location} from {self.start_time} to {self.end_time}.")


# Step 3: Create the scheduling service that will manage all types of tours.
class TourSchedulingService:
    def __init__(self):
        self.tours_by_category = {
            "Group": [],
            "KIST": [],
            "Private": []
        }

    # Method to add a tour
    def add_tour(self, tour):
        if tour.tour_type in self.tours_by_category:
            self.tours_by_category[tour.tour_type].append(tour)
        else:
            print(f"Unknown tour type: {tour.tour_type}")
            return
        tour.schedule_tour()

    # Method to list all tours in a given category
    def get_tours_by_category(self, category):
        if category in self.tours_by_category:
            return self.tours_by_category[category]
        else:
            print(f"No tours found for category: {category}")
            return []


# Example usage of the system
if __name__ == "__main__":
    # Instantiate the scheduling service
    scheduling_service = TourSchedulingService()

    # Create different tours
    group_tour = GroupTour(
        "South River High School",
        date(2024, 11, 13),
        date(2024, 11, 13),
        "Kean Hall",
        timedelta(hours=10),  # 10:00 AM
        timedelta(hours=12)   # 12:00 PM
    )

    kist_tour = KISTTour(
        "KIST",
        date(2024, 11, 11),
        date(2024, 11, 11),
        "Kean Hall",
        timedelta(hours=10),  # 10:00 AM
        timedelta(hours=12)   # 12:00 PM
    )

    private_tour = PrivateTour(
        "VIP Private Tour",
        date(2024, 11, 12),
        date(2024, 11, 12),
        "Kean Hall",
        timedelta(hours=10),  # 10:00 AM
        timedelta(hours=12)   # 12:00 PM
    )

    # Add tours to the service
    scheduling_service.add_tour(group_tour)
    scheduling_service.add_tour(kist_tour)
    scheduling_service.add_tour(private_tour)

    # Retrieve and list all KIST tours
    print("\nListing KIST Tours:")
    kist_tours = scheduling_service.get_tours_by_category("KIST")
    for tour in kist_tours:
        print(f"- {tour.tour_name} at {tour.location} from {tour.start_date} to {tour.end_date} "
              f"from {tour.start_time} to {tour.end_time}")
