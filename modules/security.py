import bcrypt


def password_hash(password):
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    

    return (salt, hash)


def check_password(salt, hashed_password, password):
    bytes = password.encode('utf-8')
    if bcrypt.hashpw(bytes,salt) == hashed_password:
        return True
    else:
        return False