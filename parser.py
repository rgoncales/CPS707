import re
def getUserFromString(string: str) -> str:
    userInfo = re.split("\s+", string)
    return {
        'username': userInfo[0],
        'type': userInfo[1],
        'credit': userInfo[2]
    }
