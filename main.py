from user import User
from typing import Dict
from utils.parser import (readAccountFile, readTicketFile)
from utils.errors import (INVALID_TRANSACTION, error)
from api import Api
from utils.settings import (
    LOGIN,
    LOGOUT,
    CREATE,
    DELETE,
    ADD_CREDIT,
    REFUND,
    SELL,
    BUY
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
    accs = readAccountFile()
    tickets = readTicketFile()

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
                accs = readAccountFile()
                tickets = readTicketFile()
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

        elif INPUT == ADD_CREDIT:
            res = api.addCredit(usr, accs)
            if res != None:
                trans.append(res['result'])
                print(res['success'])

        elif INPUT == REFUND:
            res = api.refund(usr, accs)
            if res != None:
                trans.append(res['result'])
                print(res['success'])

        elif INPUT == SELL:
            res = api.sell(usr, tickets)
            if res != None:
                trans.append(res['result'])
                print(res['success'])

        elif INPUT == BUY:
            res = api.buy(usr, tickets)
            if res != None:
                trans.append(res['result'])
                print(res['success'])
        else:
            error(INVALID_TRANSACTION)
        print('')
