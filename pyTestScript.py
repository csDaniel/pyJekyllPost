#!/usr/bin/python

from pyJekyllPost import *



def status(count, filename):
	print("Beginning test {}: \t {}".format(count, filename))

	
	
def runTest(count, filename):
	
	status(count, filename)
	# open testfile.md 
	contents = readFile(filename)

	# display the contents after opening
	print("{}".format(contents))
	lines()	

	
	
def testSuite():

	test1 = "testfile.md"
	count = 1
	runTest(count, test1)
	
	#print ("The title is: {}".format(setTitle()))
	print ("The date is: {}".format(getDate()))

testSuite()