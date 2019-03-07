from decimal import Decimal
from user import User
from utils.parser import res
from utils.permissions import accountTypes
from utils.transactions import formatTransaction
from utils.settings import (
    CREATE,
    DELETE,
    ADD_CREDIT,
    REFUND,
    AA
)

def new_user(usr, accs):
    username = input("New username: ")
    if len(username) < 4 or len(username) > 15:
        raise ValueError("Username must be 4 to 15 characters.")
    if username in accs:
        raise ValueError("Username already exists.")
    userType = input("Type [AA, FS, SS, BS]: ")
    if userType not in accountTypes:
        raise ValueError("Invalid account type.")
    newUser = User(username, userType)
    accs[username] = newUser
    trans = formatTransaction(CREATE, newUser.asJSON())
    return res(trans, "Created new user.")

def delete_user(usr, accs):
    username = input("User to delete: ")
    if usr.username == username:
        raise ValueError("Cannot delete yourself.")
    if username not in accs:
        raise ValueError("User doesn't exist.")
    deletedUser = accs[username]
    del accs[username]
    trans = formatTransaction(DELETE, deletedUser.asJSON())
    return res(trans, "Deleted user.")

def add_credit(usr, accs):
    trans = ''
    credit = Decimal(input("Enter credit amount: "))
    if credit > 1000:
        raise ValueError("Can only add $1000 per transaction.")

    if usr.type == AA:
        username = input("Enter target username: ")
        if username not in accs:
            raise ValueError("User does not exist.")
        toUser = accs[username]
        toUser.addCredit(credit)
        trans = formatTransaction(ADD_CREDIT, toUser.asJSON())
    else:
        usr.addCredit(credit)
        trans = formatTransaction(ADD_CREDIT, usr.asJSON())
    return res(trans, "Added credit to user.")

def refund_credit(usr, accs):
    fromUser = input("Refund from [username]: ")
    if fromUser not in accs:
        raise ValueError("No such user.")

    toUser = input("Refund to [username]: ")
    if toUser not in accs:
        raise ValueError("No such user.")

    amount = Decimal(input("Amount to refund: "))

    # instanciate users
    seller = accs[fromUser]
    buyer = accs[toUser]
    # charge/credit accounts
    seller.chargeCredit(amount)
    buyer.addCredit(amount)

    refundJSON = {
        'from': seller.username,
        'to': buyer.username,
        'credit': amount
    }

    trans = formatTransaction(REFUND, refundJSON)
    return res(trans, "Refunded credit to user.")
