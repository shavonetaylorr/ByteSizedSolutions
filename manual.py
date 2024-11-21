from datetime import datetime

# Example data: List of tours with details
tours = [
    {
        'tour_name': 'Campus Tour A',
        'date': '2024-11-22',
        'time': '10:00 AM',
        'location': 'Main Campus',
        'participants': ['Alice', 'Bob', 'Charlie'],
    },
    {
        'tour_name': 'Science Building Tour',
        'date': '2024-11-22',
        'time': '1:00 PM',
        'location': 'Science Building',
        'participants': ['David', 'Eve'],
    },
    {
        'tour_name': 'Library Tour',
        'date': '2024-11-23',
        'time': '11:00 AM',
        'location': 'Library',
        'participants': ['Frank', 'Grace'],
    },
    {
        'tour_name': 'Campus Tour B',
        'date': '2024-11-24',
        'time': '9:00 AM',
        'location': 'Main Campus',
        'participants': ['Hannah', 'Ivy'],
    }
]

# Function to display all tours
def display_tours(tours):
    if not tours:
        print("No tours scheduled.")
        return

    print("Scheduled Tours Breakdown:")
    print("=" * 40)
    for tour in tours:
        print(f"Tour Name: {tour['tour_name']}")
        print(f"Date: {tour['date']}")
        print(f"Time: {tour['time']}")
        print(f"Location: {tour['location']}")
        print(f"Participants: {', '.join(tour['participants'])}")
        print("-" * 40)

# Function to filter tours by date
def filter_by_date(tours, target_date):
    target_date = datetime.strptime(target_date, "%Y-%m-%d").date()  # Convert to date object for comparison
    filtered_tours = [tour for tour in tours if datetime.strptime(tour['date'], "%Y-%m-%d").date() == target_date]
    return filtered_tours

# Function to filter tours by location
def filter_by_location(tours, target_location):
    filtered_tours = [tour for tour in tours if tour['location'].lower() == target_location.lower()]
    return filtered_tours

# Main function to interact with the user
def main():
    while True:
        print("\n1. Show All Scheduled Tours")
        print("2. Filter Tours by Date")
        print("3. Filter Tours by Location")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_tours(tours)
        elif choice == '2':
            date = input("Enter the date (YYYY-MM-DD) to filter by: ")
            filtered_tours = filter_by_date(tours, date)
            display_tours(filtered_tours)
        elif choice == '3':
            location = input("Enter the location to filter by: ")
            filtered_tours = filter_by_location(tours, location)
            display_tours(filtered_tours)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
