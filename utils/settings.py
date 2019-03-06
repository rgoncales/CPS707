# Files
ACCOUNT_FILE = 'accounts.txt'
TRANSACTION_FILE = 'transactions.txt'

# Transaction types
CREATE = 'CREATE'
DELETE ='DELETE',
SELL = 'SELL',
BUY = 'BUY',
REFUND = 'REFUND',
ADD_CREDIT = 'ADD_CREDIT',
LOGOUT = 'LOGOUT'

codes = {
    CREATE : '01',
    DELETE : '02',
    SELL : '03',
    BUY : '04',
    REFUND : '05',
    ADD_CREDIT : '06',
    LOGOUT : '00',
}

def getTransactionCode(action):
    return codes[action]
