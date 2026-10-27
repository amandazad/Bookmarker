import bcrypt
from users import add_user

username = "admin"
password = "mysecretpassword01"
#converting the string password to bytes
pw_bytes = password.encode('utf-8')
#generating the salt
salt = bcrypt.gensalt()
#generating the hash
hash = bcrypt.hashpw(pw_bytes, salt)
hashed_password = hash.decode('utf-8')
print(hash)
print(add_user(username, hashed_password))