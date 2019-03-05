# Will instanciate and hold current user info
# Username, Credit, Type
class User:
    def __init__(self, username, type, credit):
        self.username = username
        self.type = type
        self.credit = credit

    def description(self):
        print("  Name: {} \n"
              "  Type: {} \n"
              "Credit: {}"
              .format(self.username, self.type, self.credit))
