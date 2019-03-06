from utils.parser import (getUserJSON, res)
from utils.permissions import accountTypes
from utils.transactions import formatTransaction
from utils.settings import CREATE

def new_user(usr, accs):
    userName = input("New username: ")
    if len(userName) < 4 or len(userName) > 15:
        raise ValueError("Username must be 4 to 15 characters.")
    if userName in accs:
        raise ValueError("Username already exists.")
    userType = input("Type [AA, FS, SS, BS]: ")
    if userType not in accountTypes:
        raise ValueError("Invalid account type.")
    newUser = getUserJSON(userName, userType)
    accs[userName] = newUser
    trans = formatTransaction(CREATE, newUser)
    return res(trans, "Created new user.\n")

def delete_user(usr, accs):
    pass

def add_credit(usr, accs):
    pass
