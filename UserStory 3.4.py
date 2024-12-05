import random

class Manager:
    def __init__(self, fulltime_workers):
        """
        Initializes the Manager with a list of full-time workers.
        :param fulltime_workers: List of full-time workers' names
        """
        self.fulltime_workers = fulltime_workers
        self.speaker_roles = {}

    def generate_speaker_role(self, role_name):
        """
        Creates a new speaker role.
        :param role_name: Name of the speaker role
        """
        if role_name in self.speaker_roles:
            print(f"Role '{role_name}' already exists.")
        else:
            self.speaker_roles[role_name] = None
            print(f"Role '{role_name}' has been created.")

    def assign_random_worker_to_role(self, role_name):
        """
        Randomly assigns a full-time worker to a speaker role.
        :param role_name: The name of the speaker role
        """
        if role_name not in self.speaker_roles:
            print(f"Role '{role_name}' does not exist. Create it first.")
        elif self.speaker_roles[role_name] is not None:
            print(f"Role '{role_name}' is already assigned to {self.speaker_roles[role_name]}.")
        elif not self.fulltime_workers:
            print("No full-time workers available for assignment.")
        else:
            worker_name = random.choice(self.fulltime_workers)
            self.speaker_roles[role_name] = worker_name
            print(f"Worker '{worker_name}' has been randomly assigned to role '{role_name}'.")

    def view_roles(self):
        """
        Displays all roles and their assigned workers.
        """
        if not self.speaker_roles:
            print("No roles have been created yet.")
        else:
            print("Speaker Roles and Assignments:")
            for role, worker in self.speaker_roles.items():
                assignment = worker if worker else "Unassigned"
                print(f"  - {role}: {assignment}")


# Example
if __name__ == "__main__":
    # List of full-time workers
    fulltime_workers = ["Alice Johnson", "Bob Smith", "Chris Evans"]

    manager = Manager(fulltime_workers)

    # Generate roles
    manager.generate_speaker_role("Student Ambassador")
    manager.generate_speaker_role("Tour Ambassador")

    # Assign workers randomly
    manager.assign_random_worker_to_role("Student Ambassador")
    manager.assign_random_worker_to_role("Tour Ambassador")

    # View roles
    manager.view_roles()
