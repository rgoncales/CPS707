from utils.parser import appendSpaces

# returns string for entry into tickets file
def getTicketFromJSON(ticketInfo):
    title = appendSpaces(ticketInfo['title'], 25, False)
    seller = appendSpaces(ticketInfo['seller'], 15, False)
    numAvailable = appendSpaces(str(ticketInfo['num']), 3, True)
    price = appendSpaces(str(ticketInfo['price']), 6, True)

    result = title + ' ' + seller + ' ' + numAvailable + ' ' + price
    return result

def getTicketJSON(title, seller, numAvailable, price):
    return {
        'title': title,
        'seller': seller,
        'num': numAvailable,
        'price': price
    }
