# Transaction types
CREATE = 'CREATE'
DELETE ='DELETE'
SELL = 'SELL'
BUY = 'BUY'
REFUND = 'REFUND'
ADD_CREDIT = 'ADD_CREDIT'
LOGOUT = 'LOGOUT'
LOGIN = 'LOGIN'

AA = 'AA'
FS = 'FS'
BS = 'BS'
SS = 'SS'

MAX_CREDIT = 999999.00
MIN_CREDIT = 0.00


class FileNames:
    def __init__(self):
        self.ACCOUNT_FILE = 'accounts.txt'
        self.TRANSACTION_FILE = 'transactions.txt'
        self.TICKET_FILE = 'tickets.txt'

filenames = FileNames()
