from user import User
from typing import Dict
from utils.settings import ACCOUNT_FILE
from utils.parser import getUserFromString
from utils.errors import (INVALID_TRANSACTION, error)
from api import Api
import pprint

usr = None
accountDict = {}
api = Api()

#for debugging
pp = pprint.PrettyPrinter(indent=4)

if __name__ == '__main__':
    #read all users on file and put them into an array
    srcFile = open(ACCOUNT_FILE, 'r')
    for line in srcFile:
        line = line.strip('\n')
        if line == 'END':
            break
        else:
            u = getUserFromString(line)
            accountDict[u['username']] = u
    srcFile.close()

    INPUT = ''
    while 1:
        INPUT = input()
        if INPUT == 'Q':
            break

        elif INPUT == "LOGIN":
            if usr != None:
                error('User already logged in.')
                continue
            res = api.login(usr, accountDict)
            if res != None:
                print(res['success'])
                usr = res['result']

        elif INPUT == "LOGOUT":
            res = api.logout(usr, accountDict)
            if res != None:
                print(res['success'])
                usr = None

        elif INPUT == "CREATE":
            res = api.create(usr, accountDict)
            if res != None:
                print(res['success'])
                newUser = res['result']
                accountDict[newUser['username']] = newUser
        else:
            error(INVALID_TRANSACTION)
