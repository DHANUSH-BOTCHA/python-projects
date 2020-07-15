from difflib import get_close_matches
from fnmatch import translate

print("Welcome to new version of the python 'Dictionary' ")

import json

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("Press 'y' for Yes or 'n' for No")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return ["No words are found"]
        else:
            return ["You have entered wrong keys.. please enter valid key"]

    else:
        print("you have pressed wrong keys")


word = input("Enter the word to search: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print("-->", item)
else:
    print("-->", output)

print(output)
