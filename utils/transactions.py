from utils.parser import appendSpaces
from utils.users import getUserFromJSON
from utils.tickets import getTicketFromJSON
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

# length 43 => 05
def type2(info):
    code = info['code']
    fromUser = appendSpaces(info['from'], 15, False)
    toUser = appendSpaces(info['to'], 15, False)
    credit = appendSpaces(str('%.2f' % info['credit']), 9, True)
    return code + ' ' + fromUser + ' ' + toUser + ' ' + credit

# length 52 => 03, 04
def type3(info):
    code = info['code']
    ticket = getTicketFromJSON(info)
    return code + ' ' + ticket

def formatTransaction(action, info):
    info['code'] = getTransactionCode(action)
    if action in {CREATE, DELETE, ADD_CREDIT, LOGOUT}:
        return type1(info)
    elif action in {REFUND}:
        return type2(info)
    elif action in {SELL, BUY}:
        return type3(info)
    return None
