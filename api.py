from login import (auth, end)
class Api:
    def login(self, user, username, dict):
        try:
            res = auth(user, username, dict)
            return res
        except Exception as e:
            print(e)

    def logout(self, user):
        try:
            res = end(user)
            return res
        except Exception as e:
            print(e)
