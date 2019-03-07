from decimal import Decimal
import utils.parser

# returns string for entry into tickets file
def getTicketFromJSON(ticketInfo):
    title = utils.parser.appendSpaces(ticketInfo['title'], 25, False)
    seller = utils.parser.appendSpaces(ticketInfo['seller'], 15, False)
    numAvailable = utils.parser.appendSpaces(str(ticketInfo['num']), 3, True)
    price = utils.parser.appendSpaces(str('%.2f' % ticketInfo['price']), 6, True)

    result = title + ' ' + seller + ' ' + numAvailable + ' ' + price
    return result

def getTicketJSON(title, seller, numAvailable, price):
    return {
        'title': title,
        'seller': seller,
        'num': int(numAvailable),
        'price': Decimal(price)
    }

def getKey(title, seller):
    key = title + '' + seller
    return key
