import json
import difflib
from difflib import get_close_matches

def indexer(word):
    word = word.lower()
    if word in dict.keys():
        return dict[word]
    elif len(get_close_matches(word,dict.keys())) > 0:
        maxr=0.0
        possible = get_close_matches(word,dict.keys())[0]
        print("Word Not Found!!","Did you mean %s instead? (y/n) :" %possible)
        choice = input()
        if choice == 'y':
            return dict[possible]
        else:
             return ["Word Not Found!!"]
    else:
        return ["Word Not Found!!"]


ch = 'y'
while ch == 'y':
    dict = json.load(open('data.json','r'))
    usin = input("Enter a word: ")
    meaning = indexer(usin)
    for mean in meaning:
        print (mean)
    ch=input("Do you wish to continue? (y/n): ")
