from user import User
from typing import Dict
from parser import getUserFromString
from settings.errors import INVALID_TRANSACTION
from settings.transactions import allTransactionsList
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
            #print (u)
            accountDict[u['username']] = u

    INPUT = ''
    while 1:
        INPUT = input()
        if INPUT == 'Q':
            break
        # only accept login
        elif INPUT == "LOGIN":
            if usr != None:
                print(INVALID_TRANSACTION)
                continue
            INPUT = input("Enter username:")
            usr = api.login(usr, INPUT, accountDict)
        elif INPUT == "LOGOUT":
            res = api.logout(usr)
            if res != None:
                print(res)
        else:
            print(INVALID_TRANSACTION)
