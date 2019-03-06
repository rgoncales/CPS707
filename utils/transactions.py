from utils.parser import getUserFromJSON
from utils.settings import (
    CREATE,
    DELETE,
    SELL,
    BUY,
    REFUND,
    ADD_CREDIT,
    LOGOUT
)

codes = {
    CREATE : '01',
    DELETE : '02',
    SELL : '03',
    BUY : '04',
    REFUND : '05',
    ADD_CREDIT : '06',
    LOGOUT : '00',
}

def getTransactionCode(action):
    return codes[action]

# length 29 => 01, 02, 06, 00
def type1(info):
    code = info['code']
    user = getUserFromJSON(info)
    return code + ' ' + user

# length ?? => 05
def type2(info):
    pass

# length ?? => 03, 04
def type3(info):
    pass

def formatTransaction(action, info):
    info['code'] = getTransactionCode(action)
    return {
        CREATE: type1(info),
        DELETE: type1(info),
        ADD_CREDIT: type1(info),
        LOGOUT: type1(info),
        REFUND: type2(info),
        SELL: type3(info),
        BUY: type3(info)
    }[action]
