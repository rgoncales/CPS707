# Will instanciate and hold user info
# Username, Credit, Type
from decimal import Decimal
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
    SS,
    MAX_CREDIT,
    MIN_CREDIT
)
from utils.permissions import getPermissions
class User:
    def __init__(self, username, type, credit = 0.00):
        self.username = username
        self.type = type
        self.credit = Decimal(credit)
        self.permissions = getPermissions(self.type)

    @classmethod
    def fromJSON(cls, userJSON):
        tempName = userJSON['username']
        tempType = userJSON['type']
        tempCredit = userJSON['credit']
        return cls(tempName, tempType, tempCredit)


    def description(self) -> None:
        print("  Name: {} \n"
              "  Type: {} \n"
              "Credit: {}"
              .format(self.username, self.type, self.credit))

    def hasPermission(self, req: str) -> bool:
        return (req in self.permissions)

    def asJSON(self):
        return {
            'username': self.username,
            'type': self.type,
            'credit': self.credit
        }

    def chargeCredit(self, amount):
        if (self.credit - amount) < MIN_CREDIT:
            raise ValueError("User does not have enough credit.")
        self.credit -= amount

    def addCredit(self, amount):
        if (self.credit + amount) > MAX_CREDIT:
            raise ValueError("Maximum credit exceeded.")
        self.credit += amount
