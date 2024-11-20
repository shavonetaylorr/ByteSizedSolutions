import random

# List of all ambassadors with their statuses
ambassadors = [
    {"name": "Joe", "status": "experienced"},
    {"name": "Joy", "status": "experienced"},
    {"name": "kendra", "status": "experienced"},
    {"name": "caylin", "status": "experienced"},
    {"name": "melia", "status": "experienced"},
    {"name": "Sara", "status": "experienced"},
    {"name": "Janai", "status": "new"},
    {"name": "delaia", "status": "new"},
    {"name": "Cece", "status": "new"},
    {"name": "Alasia", "status": "experienced"},
    {"name": "Alexis B", "status": "experienced"},
    {"name": "Alexis H", "status": "experienced"},
    {"name": "Chi chi", "status": "experienced"},
    {"name": "Eric", "status": "new"},
    {"name": "gianna", "status": "new"},
    {"name": "Jason", "status": "experienced"},
    {"name": "John", "status": "experienced"},
    {"name": "Jordan", "status": "experienced"},
    {"name": "Juliana", "status": "experienced"},
    {"name": "Kiera", "status": "new"},
    {"name": "Natalie", "status": "experienced"},
    {"name": "Salma", "status": "experienced"},
    {"name": "Samaya", "status": "new"},
    {"name": "Savannah", "status": "new"},
    {"name": "Shanice", "status": "new"},
    {"name": "Suzy", "status": "experienced"},
]

def assign_shadows(ambassadors):
    experienced = [amb["name"] for amb in ambassadors if amb["status"] == "experienced"]
    new = [amb["name"] for amb in ambassadors if amb["status"] == "new"]
    
    if len(experienced) < len(new):
        print("Not enough experienced ambassadors to assign one per new ambassador.")
        return
    
    assignments = {}
    for newbie in new:
        mentor = random.choice(experienced)
        assignments[newbie] = mentor
    

    return assignments

# Assigning new ambassadors to experienced ones
shadow_assignments = assign_shadows(ambassadors)

# Display assignments
if shadow_assignments:
    print("Tour shadowing Assignments:")
    for new_ambassador, mentor in shadow_assignments.items():
        print(f"{new_ambassador} will shadow {mentor}")


