from utils.permissions import auth
from transactions.login import (session_new, session_end)
from transactions.users import new_user
from utils.settings import (LOGOUT, CREATE)


class Api:
    def login(self, usr, dict):
        try:
            return session_new(usr, dict)
        except Exception as e:
            print(e)

    def logout(self, usr):
        try:
            auth(usr, LOGOUT)
            return session_end(usr)
        except Exception as e:
            print(e)

    def create(self, usr, dict):
        try:
            auth(usr, CREATE)
            return new_user(dict)
        except Exception as e:
            print(e)
