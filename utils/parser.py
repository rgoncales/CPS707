import re

# parse userInfo from single line
def getUserFromString(string: str) -> str:
    userInfo = re.split("\s+", string)
    return {
        'username': userInfo[0],
        'type': userInfo[1],
        'credit': userInfo[2]
    }

# returns string for entry into accounts file
def getStringFromJSON(userInfo):
    userName = appendSpaces(userInfo['username'], 15, False)
    userType = appendSpaces(userInfo['type'], 2, False)
    userCredit = appendSpaces(str(userInfo['credit']), 9, True)

    result = userName + ' ' + userType + ' ' + userCredit
    return result

# append spaces to make line proper length
def appendSpaces(str: str, length:int, rightAlign: bool) -> str:
    spaces = length - len(str)
    if rightAlign:
        for i in range(0, spaces):
            str = ' ' + str
    else:
        for i in range(0, spaces):
            str += ' '
    return str

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
