from db.users import *
from modules.security import *


def sign_up(username, password):

    if get_user(username) != None:
        raise Exception("User Already Exists")

    (salt, hash) = password_hash(password)

    create_user(username, hash, salt)



def log_in(username, password):
    res = get_user(username)

    if res == None:
        raise ValueError("User Does Not Exist")
    

    if check_password(res[3], res[2], password):
        return True
    else:
        raise ValueError("Incorrect Password")
