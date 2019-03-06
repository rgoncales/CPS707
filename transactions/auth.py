from user import User
from utils.parser import res, getStringFromJSON
from utils.settings import ACCOUNT_FILE

def session_new(usr, accounts):
    if usr != None:
        raise ValueError("User already logged in.")
    username = input("Enter username:")
    if username not in accounts:
        raise ValueError("User not found.")
    entry = accounts[username]
    user = User(entry['username'], entry['type'], entry['credit'])
    return res(user, 'Logged in.\n')

def session_end(usr, accounts):
    # write accounts file
    f = open(ACCOUNT_FILE, 'w')
    for key, value in accounts.items():
        f.write(getStringFromJSON(value)+'\n')
    f.write('END')
    f.close()

    return res(None, 'Session finished.\n')
