from utils.settings import (
    LOGOUT,
    CREATE,
    DELETE,
    SELL,
    BUY,
    REFUND,
    ADD_CREDIT
)

accountTypes = {'AA', 'FS', 'BS', 'SS'}

# Admin permissions
def AA():
    return {
        LOGOUT,
        CREATE,
        DELETE,
        SELL,
        BUY,
        REFUND,
        ADD_CREDIT
    }

# Full-Standard permissions
def FS():
    return {
        LOGOUT,
        SELL,
        BUY,
        REFUND,
        ADD_CREDIT,
    }

# Buy-Standard permissions
def BS():
    return {
        LOGOUT,
        BUY,
        REFUND,
        ADD_CREDIT,
    }

# Sell_Standard permissions
def SS():
    return {
        LOGOUT,
        SELL,
        REFUND,
        ADD_CREDIT,
    }

def getPermissions(userType):
    return {
        'AA': AA(),
        'FS': FS(),
        'BS': BS(),
        'SS': SS(),
    }[userType]

def auth(usr, req):
    if usr == None:
        raise ValueError("User must be logged in.")
    elif not usr.hasPermission(req):
        raise ValueError("Transaction not permitted.")
