import json
from difflib import get_close_matches as match

dataDict = json.load(open("data.json"))

def dictionary(word):
    word = word.lower()

    if(word in dataDict):
        return dataDict[word]

    elif(len(match(word, dataDict.keys(), cutoff=0.8)) > 0):
        answer = input("Did you mean %s ? Y/N: " % match(word, dataDict.keys())[0])
        if(answer == "Y" or answer == "y"):
            return dataDict[match(word, dataDict.keys())[0]]
        elif(answer == "N" or answer == "n"):
            return "The word doesn't exist!"
        else:
            return "Error!"

    else:
        return "The word doesn't exist!"

word = input("Enter word: ")

output = dictionary(word)

if(type(output) == list):
    for i in output:
        print(i)
else:
    print(output)
