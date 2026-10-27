from utils import load_data_users, update_data_users
from users import *
import bcrypt

def validate_user(user: str, password: str) -> bool:
    users = load_data_users()
    if users:
        for id, obj in users.items():
            if obj["user"] == user:
                # Verify the password against the stored hash
                check_validation = bcrypt.checkpw(password.encode('utf-8'), obj["password"].encode('utf-8'))
                if check_validation:
                    return True
                else:
                    return False
        return False
    else:
        return False