from user import User
from typing import Dict
from parser import getUserFromString
from settings.errors import INVALID_TRANSACTION

currentUser = None
ACCOUNT_FILE = 'accounts.txt'
TRANSACTION_FILE = 'transactions.txt'
accountDict = {}

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
        INPUT = input("\n")
        if INPUT == 'Q':
            break
        if currentUser is None:
            # only accept login
            if INPUT == "LOGIN":
                INPUT = input("\nEnter username:")
                if INPUT in accountDict:
                    print("Logged in!")
                    currentUser = User(u['username'], u['type'], u['credit'])
                else:
                    print("No such user.")
        else:
            print(INVALID_TRANSACTION)
