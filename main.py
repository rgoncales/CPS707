from user import User
from typing import Dict
from parser import getUserFromString

currentUser = User
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
            print (u)
            accountDict[u['username']] = u

    USER_INPUT = ''
    while 1:
        USER_INPUT = input("\nEnter username:")
        if USER_INPUT == 'Q':
            break
        if USER_INPUT in accountDict:
            currentUser = User(u['username'], u['type'], u['credit'])
