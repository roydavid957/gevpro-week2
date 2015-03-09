#!/usr/bin/python3

import sys
import json
from collections import namedtuple

"""a program which finds blood and die matches of several languages"""
def main():
    
    """open file"""
    open_file = open("blood-die.json", "r")
    filedata = json.load(open_file)

    country = namedtuple("country", "language, classifications")
    
    resultsList = []
    
    """making lists of all the blood and die words"""
    for langList in filedata:
        name = langList[0]
        classification = langList[1]
        bloodWords = langList[2].strip().split(",")
        dieWords = langList[3].strip().split(",")
        
        """if bloodword matches dieword append to resultsList"""
        for blood in bloodWords:
            for die in dieWords:
               if blood==die:
                    resultsList.append(country(name, classification))
                    
    print([language for (language, classifications) in resultsList])
    
if __name__ == "__main__":
	main()
