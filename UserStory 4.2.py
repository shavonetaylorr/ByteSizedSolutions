class Ambassador:
    def __init__(self, name, experience_level):
        self.name = name
        self.experience_level = experience_level.lower()
        self.role = None
        self.assign_role()

    def assign_role(self):
        if self.experience_level == "experienced":
            self.role = "Lead Ambassador"
        else:
            self.role = "Assistant Ambassador"

    def get_name(self):
        return self.name

    def get_experience_level(self):
        return self.experience_level

    def get_role(self):
        return self.role

    def __str__(self):
        experience_capitalized = self.experience_level.capitalize()
        return f"{self.name}_{experience_capitalized} - Role: {self.role}"


class Manager:
    def __init__(self):
        self.ambassadors = []

    def add_ambassador(self, ambassador):
        self.ambassadors.append(ambassador)

    def display_ambassadors(self):
        for ambassador in self.ambassadors:
            print(ambassador)


if __name__ == "__main__":
    manager = Manager()
    ambassador1 = Ambassador("James", "New")
    ambassador2 = Ambassador("Garna", "Experienced")

    manager.add_ambassador(ambassador1)
    manager.add_ambassador(ambassador2)

    manager.display_ambassadors()
