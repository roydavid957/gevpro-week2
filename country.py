#!/usr/bin/python3
import sys

class Country():
  def __init__(self, country):
    self.country = country
    
  def __str__(self):
    return "Hello from {0}".format(self.country)
  
def main(argv):
	if len(argv) == 2:
		country = argv[1]
		ex = Country(country)
		print(ex)
  
if __name__ == "__main__":
  main(sys.argv)
