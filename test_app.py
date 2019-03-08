import app
import api
from actions import (auth, tickets, users)
from utils.settings import filenames
import sys

if __name__ == '__main__':
    INPUT_NAME = sys.argv[1]

    inputList = []
    inFile = open(INPUT_NAME, 'r')
    for line in inFile:
        inputList.append(line.strip('\n'))
    inputList.append('Q')
    inputList.reverse()

    outputList = []
    def mock_input(query = ''):
        string = ''
        if query != '':
            string = query
        testInput = inputList.pop()
        if testInput != 'Q':
            if string == None:
                string = testInput
            else:
                string += testInput
            outputList.append(string)
        return testInput

    def mock_print(out = ''):
        outputList.append(out)

    # overwrite input
    app.input = mock_input
    auth.input = mock_input
    tickets.input = mock_input
    users.input = mock_input
    # overwrite print
    app.print = mock_print
    auth.print = mock_print
    tickets.print = mock_print
    users.print = mock_print
    api.print = mock_print

    filenames.ACCOUNT_FILE = 'mock_accounts.txt'
    filenames.TICKET_FILE = 'mock_tickets.txt'
    filenames.TRANSACTION_FILE = 'mock_transactions.txt'

    app.main()

    for item in outputList:
        print(item)
