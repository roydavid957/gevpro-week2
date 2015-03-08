#!/usr/bin/python3

import sys
import json
from collections import namedtuple

"""check if bloodword is in dieword, if so return True for that word"""
def bloodISdie(lang):
    
    blood = lang[2].split()
    die = lang[3].split()
    return [True for word in blood if word in die]

def main():
    
    language = namedtuple("language", "name, classification")
    
    """open jsonfile"""
    jsonOpen = open("blood-die.json", "r")
    jsonFile = json.load(jsonOpen)
    
    """add every word to list if bloodISdie returns True for that word"""
    resultlist = []
    [resultlist.append(language(lang[0], lang[1])) for lang in jsonFile if bloodISdie(lang)]
    
    """used 2 tabs to clearify both results"""
    [print(result.name, "		", result.classification) for result in resultlist]
    
if __name__ == "__main__":
	main()
