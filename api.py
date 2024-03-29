from utils.permissions import auth
from actions.auth import (session_new, session_end)
from actions.users import (new_user, delete_user, add_credit, refund_credit)
from actions.tickets import (sell_ticket, buy_ticket)
from utils.settings import (
    LOGOUT,
    CREATE,
    DELETE,
    ADD_CREDIT,
    REFUND,
    SELL,
    BUY
)

class Api:
    def login(self, usr, accs):
        try:
            return session_new(usr, accs)
        except Exception as e:
            print(e)

    def logout(self, usr, accs, trans, tickets):
        try:
            auth(usr, LOGOUT)
            return session_end(usr, accs, trans, tickets)
        except Exception as e:
            print(e)

    def create(self, usr, accs):
        try:
            auth(usr, CREATE)
            return new_user(usr, accs)
        except Exception as e:
            print(e)

    def delete(self, usr, accs):
        try:
            auth(usr, DELETE)
            return delete_user(usr, accs)
        except Exception as e:
            print(e)

    def addCredit(self, usr, accs):
        try:
            auth(usr, ADD_CREDIT)
            return add_credit(usr, accs)
        except Exception as e:
            print(e)

    def refund(self, usr, accs):
        try:
            auth(usr, REFUND)
            return refund_credit(usr, accs)
        except Exception as e:
            print(e)

    def sell(self, usr, tickets):
        try:
            auth(usr, SELL)
            return sell_ticket(usr, tickets)
        except Exception as e:
            print(e)

    def buy(self, usr, tickets):
        try:
            auth(usr, BUY)
            return buy_ticket(usr, tickets)
        except Exception as e:
            print(e)
