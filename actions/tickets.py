from decimal import Decimal
from utils.parser import res
from utils.tickets import getTicketJSON
from utils.transactions import formatTransaction
from utils.settings import SELL

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

    newTicket = getTicketJSON(title, usr.getUsername(), numAvailable, price)
    tickets[title] = newTicket
    trans = formatTransaction(SELL, newTicket)
    return res(trans, "Added new tickets for sale.\n")

def buy_tickets(usr, tickets):
    pass

def refund_tickets(usr, accs, tickets):
    pass
