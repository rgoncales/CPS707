from user import User
from utils.parser import res, getUserFromJSON
from utils.transactions import formatTransaction
from utils.settings import (
    ACCOUNT_FILE,
    TRANSACTION_FILE,
    LOGOUT
)

def session_new(usr, accs):
    if usr != None:
        raise ValueError("User already logged in.")
    username = input("Enter username:")
    if username not in accs:
        raise ValueError("User not found.")
    entry = accs[username]
    user = User(entry['username'], entry['type'], entry['credit'])
    return res(user, 'Logged in.\n')

def session_end(usr, accs, trans):
    # write accs file
    f = open(ACCOUNT_FILE, 'w')
    for key, value in accs.items():
        f.write(getUserFromJSON(value)+'\n')
    f.write('END')
    f.close()

    logout = formatTransaction(LOGOUT, usr.getUserJSON())
    trans.append(logout)
    # write transactions file
    f = open(TRANSACTION_FILE, 'w')
    for value in trans:
        f.write(value+'\n')
    f.close()

    return res(None, 'Session finished.\n')
