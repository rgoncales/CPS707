import re
from decimal import Decimal
from user import User
from utils.settings import (ACCOUNT_FILE, TICKET_FILE)
from utils.tickets import getKey

# get accounts from input file
def readAccountFile():
    accs = {}
    srcFile = open(ACCOUNT_FILE, 'r')
    for line in srcFile:
        line = line.strip('\n')
        if line == 'END':
            break
        else:
            u = getUserFromString(line)
            accs[u.username] = u
    srcFile.close()
    return accs

# parse userInfo from single line
def getUserFromString(string: str) -> str:
    userInfo = re.split("\s+", string)
    userJSON = {
        'username': userInfo[0],
        'type': userInfo[1],
        'credit': Decimal(userInfo[2])
    }
    return User.fromJSON(userJSON)

# get tickets from input file
def readTicketFile():
    tickets = {}
    srcFile = open(TICKET_FILE, 'r')
    for line in srcFile:
        line = line.strip('\n')
        if line == 'END':
            break
        else:
            t = getTicketFromString(line)
            key = getKey(t['title'], t['seller'])
            tickets[key] = t
    srcFile.close()
    return tickets

# parse ticketInfo from single line
def getTicketFromString(string: str) -> str:
    ticketInfo = re.split("\s+", string)
    return {
        'title': ticketInfo[0],
        'seller': ticketInfo[1],
        'num': int(ticketInfo[2]),
        'price': Decimal(ticketInfo[3])
    }

# append spaces to make line proper length
def appendSpaces(str: str, length:int, rightAlign: bool) -> str:
    spaces = length - len(str)
    if rightAlign:
        for i in range(0, spaces):
            str = '0' + str
    else:
        for i in range(0, spaces):
            str += ' '
    return str

# returns a formatted result dict
def res(result, successMsg = ''):
    response = {}
    response['result'] = result
    response['success'] = successMsg
    return response
