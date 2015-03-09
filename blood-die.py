#!/usr/bin/python3

import sys
import json
from collections import namedtuple

def main():
	open_file = open("blood-die.json", "r")
	filedata = json.load(open_file)
	
	Language = namedtuple("Country", "name, classification, blood, die")
	
	resultsList = []
	
	for language in filedata:
		country = language[0]
		classification = language[1]
		bloodWords = language[2].split(",")
		dieWords = language[3].split(",")
		[resultsList.append(Language(country, classification, blood, die)) for blood in bloodWords if blood in dieWords]
	print(resultsList)

if __name__ == "__main__":
	main()
