#cleareance levels
CREATE = '01'
DELETE = '02'
SELL = '03'
BUY = '04'
REFUND = '05'
ADD_CREDIT = '06'
LOGOUT = '00'

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
