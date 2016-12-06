#!/usr/bin/env python

import datetime
import json
import tempurature as temp
import menu as m

DATE = datetime.datetime.now()
REPEAT = "Would you like to do anything else?"

print("What is your name")
NAME = input()

print("\nHello " + name + ", welcome to PyMenu")
print("Please make your selection from the menu below")
	
if __name__ == "__main__":
	m.menu
