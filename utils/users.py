import utils.parser

# returns string for entry into accounts file
def getUserFromJSON(userInfo):
    userName = utils.parser.appendSpaces(userInfo['username'], 15, False)
    userType = utils.parser.appendSpaces(userInfo['type'], 2, False)
    userCredit = utils.parser.appendSpaces(str(userInfo['credit']), 9, True)

    result = userName + ' ' + userType + ' ' + userCredit
    return result

# creates a JSON from userInfo
def getUserJSON(name, userType, credit = 0.00):
    return {
        'username': name,
        'type': userType,
        'credit': credit
    }
