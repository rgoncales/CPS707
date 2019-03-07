from utils.parser import res
from utils.users import getUserJSON
from utils.permissions import accountTypes
from utils.transactions import formatTransaction
from utils.settings import (CREATE, DELETE)

def new_user(usr, accs):
    username = input("New username: ")
    if len(username) < 4 or len(username) > 15:
        raise ValueError("Username must be 4 to 15 characters.")
    if username in accs:
        raise ValueError("Username already exists.")
    userType = input("Type [AA, FS, SS, BS]: ")
    if userType not in accountTypes:
        raise ValueError("Invalid account type.")
    newUser = getUserJSON(username, userType)
    accs[username] = newUser
    trans = formatTransaction(CREATE, newUser)
    return res(trans, "Created new user.\n")

def delete_user(usr, accs):
    username = input("User to delete: ")
    if usr.username == username:
        raise ValueError("Cannot delete yourself.")
    if username not in accs:
        raise ValueError("User doesn't exist.")
    deletedUser = accs[username]
    del accs[username]
    trans = formatTransaction(DELETE, deletedUser)
    return res(trans, "Deleted user.\n")

def add_credit(usr, accs):
    pass
