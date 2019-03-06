from utils.permissions import auth
from actions.auth import (session_new, session_end)
from actions.users import new_user
from utils.settings import (LOGOUT, CREATE)


class Api:
    def login(self, usr, accs):
        try:
            return session_new(usr, accs)
        except Exception as e:
            print(e)

    def logout(self, usr, accs, trans):
        try:
            auth(usr, LOGOUT)
            return session_end(usr, accs, trans)
        except Exception as e:
            print(e)

    def create(self, usr, accs):
        try:
            auth(usr, CREATE)
            return new_user(usr, accs)
        except Exception as e:
            print(e)
