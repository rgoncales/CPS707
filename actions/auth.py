from user import User
from utils.parser import res
from utils.transactions import formatTransaction
from utils.users import getUserFromJSON
from utils.tickets import getTicketFromJSON
from utils.settings import (
    filenames,
    LOGOUT
)

def session_new(usr, accs):
    if usr != None:
        raise ValueError("User already logged in.")
    username = input("Enter username: ")
    if username not in accs:
        raise ValueError("User not found.")
    user = accs[username]
    return res(user, 'Logged in.')

def session_end(usr, accs, trans, tickets):
    # write accs file
    f = open(filenames.ACCOUNT_FILE, 'w')
    for key, value in accs.items():
        f.write(getUserFromJSON(value.asJSON())+'\n')
    f.write('END')
    f.close()

    logout = formatTransaction(LOGOUT, usr.asJSON())
    trans.append(logout)
    # write transactions file
    f = open(filenames.TRANSACTION_FILE, 'w')
    for value in trans:
        f.write(value+'\n')
    f.close()

    # write tickets file
    f = open(filenames.TICKET_FILE, 'w')
    for key, value in tickets.items():
        f.write(getTicketFromJSON(value)+'\n')
    f.write('END')
    f.close()

    return res(None, 'Session finished.')
