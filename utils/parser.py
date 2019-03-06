import re

# parse userInfo from single line
def getUserFromString(string: str) -> str:
    userInfo = re.split("\s+", string)
    return {
        'username': userInfo[0],
        'type': userInfo[1],
        'credit': userInfo[2]
    }

# creates a JSON from userInfo
def getUserJSON(name, userType, credit = 0.00):
    return {
        'username': name,
        'type': userType,
        'credit': credit
    }

# returns a formatted result dict
def res(result, successMsg = ''):
    response = {}
    response['result'] = result
    response['success'] = successMsg
    return response
