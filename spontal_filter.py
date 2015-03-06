#!/usr/bin/python3

import xml.etree.ElementTree as ET
import sys

def main(argv):
	
	#import data
    tree = ET.parse(argv[1])
    root = tree.getroot()
	
	#loop to compare the start and end to
	#the TOP and BOTTOM
    for POINT in root.findall('POINT'):
        
		#give grand-childs a variable  
        top = float(POINT.find('TOP_HZ').text)
        bottom = float(POINT.find('BOTTOM_HZ').text)
        start = float(POINT.find('F0_START').text)
        end = float(POINT.find('F0_END').text)
		
        if start > top or start < bottom:
            root.remove(POINT)
        elif end > top or end < bottom:
            root.remove(POINT)
	
	#write the output to a different file		
    tree.write(argv[2])

if __name__ == "__main__":
	main(sys.argv)
