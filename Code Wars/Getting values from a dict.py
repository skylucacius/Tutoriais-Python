# Given: an array containing hashes of names
# Return: a string formatted as a list of names separated by commas except for the last two names, 
# which should be separated by an ampersand.

def namelist(dictList:list):
    # for name in names:
    #     print(name[0], name[1])
    remaningItems = len(dictList)
    resultString = ''
    for dicionario in dictList:
        if remaningItems == 1 and len(dictList) >= 2:
            resultString += ' & ' + dicionario['name']
            break
        if resultString != '':
            resultString += ', ' + dicionario['name']
        else:
            resultString = dicionario['name']
        remaningItems-=1
    return resultString


# print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))
print(namelist([ {'name': 'Homer'},{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))
import test
