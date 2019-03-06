from user import User
from typing import Dict
from utils.parser import getUserFromString
from utils.errors import (INVALID_TRANSACTION, error)
from utils.transactions import allTransactionsList
from api import Api

usr = None
ACCOUNT_FILE = 'accounts.txt'
TRANSACTION_FILE = 'transactions.txt'
accountDict = {}
api = Api()

if __name__ == '__main__':
    #read all users on file and put them into an array
    srcFile = open(ACCOUNT_FILE, "r");
    for line in srcFile:
        line = line.strip('\n')
        if line == 'END':
            break
        else:
            u = getUserFromString(line)
            accountDict[u['username']] = u

    INPUT = ''
    while 1:
        INPUT = input()
        if INPUT == 'Q':
            break
        # only accept login
        elif INPUT == "LOGIN":
            if usr != None:
                error('User already logged in.')
                continue
            usr = api.login(usr, accountDict)
        elif INPUT == "LOGOUT":
            res = api.logout(usr)
            if res != None:
                print(res)
                usr = None
        elif INPUT == "CREATE":
            res = api.create(usr)
        else:
            error(INVALID_TRANSACTION)
