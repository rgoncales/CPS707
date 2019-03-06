from utils.parser import (getUserJSON, res)
from utils.permissions import accountTypes

def new_user(accounts):
    userName = input("New username: ")
    if len(userName) < 4 or len(userName) > 15:
        raise ValueError("Username must be 4 to 15 characters.")
    if userName in accounts:
        raise ValueError("Username already exists.")
    userType = input("Type [AA, FS, SS, BS]: ")
    if userType not in accountTypes:
        raise ValueError("Invalid account type.")
    newUser = getUserJSON(userName, userType)
    return res(newUser, "Created new user.\n")

def delete_user(username):
    pass

def add_credit(username, credit):
    pass
