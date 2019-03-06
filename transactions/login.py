from user import User

def session_new(usr, accountDict):
    if usr != None:
        raise ValueError("User already logged in.")
    username = input("Enter username:")
    if username not in accountDict:
        raise ValueError("User not found.")
    entry = accountDict[username]
    return User(entry['username'], entry['type'], entry['credit'])

def session_end(usr):
    return "Session finished."
