from decimal import Decimal
from utils.parser import res
from utils.tickets import (getTicketJSON, getKey)
from utils.transactions import formatTransaction
from utils.settings import (SELL, BUY)

def sell_ticket(usr, tickets):
    title = input("Event title: ")
    if len(title) < 4 or len(title) > 25:
        raise ValueError("Title must be 4 to 25 characters.")

    numAvailable = int(input("Tickets available: "))
    if numAvailable > 100:
        raise ValueError("Max number of tickets is 100.")

    price = Decimal(input("Event price (00.00): "))
    if price < 0 or price > 999.99:
        raise ValueError("Price must be 0.00 to 999.99.")

    newTicket = getTicketJSON(title, usr.username, numAvailable, price)
    key = getKey(title, usr.username)
    tickets[key] = newTicket
    trans = formatTransaction(SELL, newTicket)
    return res(trans, "Added new tickets for sale.")

def buy_ticket(usr, tickets):
    title = input("Event title: ")
    numPurchased = int(input("Tickets required: "))
    seller = input("Enter seller name: ")

    key = getKey(title, seller)
    if numPurchased > 4:
        raise ValueError("Only allowed 4 tickets per transaction.")
    if key not in tickets:
        raise ValueError("No such event.")
    event = tickets[key]
    if event['num'] < numPurchased:
        raise ValueError("Not enough tickets for sale.")

    totalCost = numPurchased * event['price']
    confirm = input("Total cost: [${}]. Continue [Y][N]: ".format(totalCost))

    if confirm == 'Y':
        # update all records
        usr.chargeCredit(totalCost)
        event['num'] -= numPurchased
        tickets[key] = event
        trans = formatTransaction(BUY, event)
        return res(trans, "Purchased tickets.")
    else:
        print("Purchase cancelled.")
