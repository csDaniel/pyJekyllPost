#!/usr/bin/python

from pyJekyllPost import *
import sys


def status(count, filename):
	print("Beginning test {}: \t {}".format(count, filename))

	
	
def runTest(count, filename):
	
	status(count, filename)
	# open testfile.md 
	contents = readFile(filename)

	# display the contents after opening
	print("{}".format(contents))
	lines()	


#test for config
def configTestNew(filename):
	configOpen(filename)
	
def configTestOpen(filename):
	lines()
	print ("Testing Config Class Object...")

	try:
		file = open(filename, "r")
	except IOError:
		print("IO ERROR")
		sys.exit()
	else:
		configFile = file.read()
			
	config = configOpen(filename)
	
	n = False 
	if config.outputLocation not in configFile:
		print ("Error: \n\t Output Location is: {}".format(config.outputLocation))
		n = True 
	for each in config.layouts:
		if each not in configFile:
			print("Error: \n\t Layouts are: {}".format(config.layouts))
			n = True 
	for each  in config.categories:
		if each not in configFile:
			print("Error: \n\t Categories are: {}".format(config.categories))
			n = True 
		
	if n is True:
		print ("FAIL")
	else:
		print ("PASS")		
	
	
def testSuite():

	test1 = "testfile.md"
	count = 1
	#runTest(count, test1)
	
	#print ("The title is: {}".format(setTitle()))
	print ("The date is: {}".format(getDate()))
	configTestOpen('config')
	configTestNew('cofig')
	
	
testSuite()