import CLI
from utils import load_data_users, update_data_users


def add_user(user: str, password: str) -> str:
    new_id = 0
    users = load_data_users()
    if users:
        for id, obj in users.items():
            if obj["user"] == user:
                return("This user already exists in the system. Please try again.")
        new_id = str(max(map(int, users.keys())) + 1)
    else:
        new_id = "1"
    users.update({str(new_id): {"user": user, "password": password}})
    update_data_users(users)
    return("You've added a new user to the system. Your user ID is: " + str(new_id))