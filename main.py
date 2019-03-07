from user import User
from typing import Dict
from utils.parser import getUserFromString
from utils.errors import (INVALID_TRANSACTION, error)
from api import Api
from utils.settings import (
    ACCOUNT_FILE,
    LOGIN,
    LOGOUT,
    CREATE,
    DELETE,
    SELL
)
import pprint

usr = None
accs = {}
tickets = {}
trans = []
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
            accs[u['username']] = u
    srcFile.close()

    INPUT = ''
    while 1:
        INPUT = input()
        if INPUT == 'Q':
            break

        elif INPUT == LOGIN:
            if usr != None:
                error('User already logged in.')
                continue
            res = api.login(usr, accs)
            if res != None:
                print(res['success'])
                usr = res['result']

        elif INPUT == LOGOUT:
            res = api.logout(usr, accs, trans, tickets)
            if res != None:
                usr = None
                trans = []
                print(res['success'])

        elif INPUT == CREATE:
            res = api.create(usr, accs)
            if res != None:
                trans.append(res['result'])
                print(res['success'])

        elif INPUT == DELETE:
            res = api.delete(usr, accs)
            if res != None:
                trans.append(res['result'])
                print(res['success'])

        elif INPUT == SELL:
            res = api.sell(usr, tickets)
            if res != None:
                trans.append(res['result'])
                print(res['success'])
        else:
            error(INVALID_TRANSACTION)
