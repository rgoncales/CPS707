from utils.settings import (
    LOGOUT,
    CREATE,
    DELETE,
    SELL,
    BUY,
    REFUND,
    ADD_CREDIT,
    AA,
    FS,
    BS,
    SS
)

accountTypes = {AA, FS, BS, SS}

# Admin permissions
def AA_permission():
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
def FS_permission():
    return {
        LOGOUT,
        SELL,
        BUY,
        REFUND,
        ADD_CREDIT,
    }

# Buy-Standard permissions
def BS_permission():
    return {
        LOGOUT,
        BUY,
        REFUND,
        ADD_CREDIT,
    }

# Sell_Standard permissions
def SS_permission():
    return {
        LOGOUT,
        SELL,
        REFUND,
        ADD_CREDIT,
    }

def getPermissions(userType):
    return {
        AA: AA_permission(),
        FS: FS_permission(),
        BS: BS_permission(),
        SS: SS_permission(),
    }[userType]

def auth(usr, req):
    if usr == None:
        raise ValueError("User must be logged in.")
    elif not usr.hasPermission(req):
        raise ValueError("Transaction not permitted.")
