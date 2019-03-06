from user import User
from utils.parser import res

def session_new(usr, accounts):
    if usr != None:
        raise ValueError("User already logged in.")
    username = input("Enter username:")
    if username not in accounts:
        raise ValueError("User not found.")
    entry = accounts[username]
    user = User(entry['username'], entry['type'], entry['credit'])
    return res(user, 'Logged in.\n')

def session_end(usr):
    return res(None, 'Session finished.\n')
