# Will instanciate and hold user info
# Username, Credit, Type
from utils.settings import (
    LOGOUT,
    CREATE,
    DELETE,
    SELL,
    BUY,
    REFUND,
    ADD_CREDIT,
    AA,
    FS,
    BS,
    SS
)
from utils.permissions import getPermissions
class User:
    def __init__(self, username, type, credit):
        self.username = username
        self.type = type
        self.credit = credit
        self.permissions = getPermissions(self.type)

    def description(self) -> None:
        print("  Name: {} \n"
              "  Type: {} \n"
              "Credit: {}"
              .format(self.username, self.type, self.credit))

    def hasPermission(self, req: str) -> bool:
        return (req in self.permissions)

    def getUserJSON(self):
        return {
            'username': self.username,
            'type': self.type,
            'credit': self.credit
        }

    def chargeCredit(self, amount):
        self.credit -= amount

    def addCredit(self, amount):
        self.credit += amount
