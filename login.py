from user import User

def auth(user, username, accountDict):
    if user != None:
        raise ValueError("User already logged in.")
    if username not in accountDict:
        raise ValueError("User not found.")
    entry = accountDict[username]
    return User(entry['username'], entry['type'], entry['credit'])

def end(user):
    if (user == None) or (not user.hasPermission('LOGOUT')):
        raise ValueError("Nobody is logged in.")
    return "Session finished."
