#!/usr/bin/python

import databaseManager
import sys
import re
import string
import datetime

PROMPT = "Enter search word here: "

def printlogo():
    print("webo - search engine: testing phase : "+str(datetime.datetime.now()))

def showData(vector):
	count = 1
	for data in vector:
		print(str(count)+". "+vector)

def retriveData(searchword):
	returnedVector = []
	data = databaseManager.viewall()
	for line in data:
		if searchword in line:
			print("found word")
			d = str(line).split(",")
			print(d)
			returnedVector.append(d[0])
	showData(returnedVector)

def run():
    printlogo()
    inputdata = raw_input(PROMPT)
    while "exit" not in inputdata:		
	retriveData(inputdata)
	inputdata = raw_input(PROMPT)
    
    

#Testing code
run()
