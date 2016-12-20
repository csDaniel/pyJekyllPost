#!/usr/bin/python

from pyJekyllPost import *
import sys
from pyJPconfig import *

def status(count, filename):
	print("Beginning test {}: \t {}".format(count, filename))
	
def configTestOpen(filename):
	lines()
	print("Testing of Configuration...")

	try:
		file = open(filename, "r")
	except IOError:
		print("IO ERROR")
		sys.exit()
	else:
		configFile = file.read()
		file.close()
	
	story = Story()
	story.configOpen(filename)
	
	n = False 
	if story.location not in configFile:
		print ("Error: \n\t Output Location is: {}".format(story.location))
		n = True 
	for each in story.layouts:
		if each not in configFile:
			print("Error: \n\t Layouts are: {}".format(story.layouts))
			n = True 
	for each  in story.categories:
		if each not in configFile:
			print("Error: \n\t Categories are: {}".format(story.categories))
			n = True 
		
	if n is True:
		print("Results...\t FAIL")
	else:
		print("Results...\t PASS")
	
def storyTestContent(filename):
	lines()
	print("Testing of Content...")
	
	try:
		file = open(filename, "r")
	except IOError:
		print("IO Error")
		sys.exit()
	else:
		rawContent = file.read()
		file.close()
	
	story = Story()
	story.getContent(filename)
	
	n = False
	if story.content not in rawContent:
		print("Error: \n\t Content does not match:\n{}\n".format(story.content, rawContent))
		n = True
		
	if n is True:
		print("Results...\t FAIL")
	else:
		print("Results...\t PASS")

def storyTestTitle(title):
	lines()
	print("Testing of Title...")
	
	story = Story()
	story.setTitle(title)
	if story.title is None:
		print("Results...\t FAIL")
	else:
		print("Results...\t PASS")

def storyTestDate():
	lines()
	print("Testing of Date...")
	
	story = Story()
	story.setDate()
	if story.date is None:
		print("Results...\t FAIL")
	else:
		print("Results...\t PASS")

def writeFileTest(content, config, title):
	lines()
	print("Testing of File Writing...")
	
	# preserve original content of the file
	try: 
		f = open(content, 'r')
	except IOError:
		errorMessage("Cannot Open File", "Filename is incorrect or file cannot be read")
	else:
		with f as d:
			rawContent = d.read()
		f.close()
		
	story = Story()
	story.setDate()
	story.setTitle(title)
	story.configOpen(config)
	story.getContent(content)
	story.saveStory(content)
	
	try: 
		f = open(content, 'r')
	except IOError:
		errorMessage("Cannot Open File", "Filename is incorrect or file cannot be read")
	else:
		with f as d:
			newContent = d.read()
		f.close()
	
	n = False
	if rawContent not in newContent:
		print("Error: \n\t Content does not match:\n{}\n{}".format(rawContent, newContent))
		n = True
		
	if n is True:
		print("Results...\t FAIL")
	else:
		print("Results...\t PASS")
	
	# return original content
	try:
		f = open(content, 'w')
	except IOError:
		errorMessage("Cannot Open File", "Filename is incorrect or file cannot be read")
	else:
		f.write(rawContent)
		f.close()

def configOpen(location):
	lines()
	print("Testing of Config Location Reading...")
	config = Config()
	oldCategories = list(config.categories)
	oldLayouts = list(config.layouts)
	
	config.getLoc(location)	
	
	n = False
	if len(config.categories) > 0: 
		if set(config.categories) == set(oldCategories):
			print("Error: \n\t Categories unchanged:\n{}\n{}".format(oldCategories, config.categories))
			n = True
	else:
		n = True
	if len(config.layouts) > 0:
		if set(config.layouts) == set(oldLayouts):
			print("Error: \n\t Layouts unchanged:\n{}\n{}".format(oldLayouts, config.layouts))
			n = True
	else:
		n = True
	
	if n is True:
		print("Results...\t FAIL")
	else:
		print("Results...\t PASS")	
		
def configAddLayoutCategory(location, newOption):
	lines()
	print("Testing adding layout and category to config")
	config = Config()
	config.getLoc(location)	
	
	oldCategories = list(config.categories)
	oldCategories.append(newOption)
	
	oldLayouts = list(config.layouts)
	oldLayouts.append(newOption)
	
	config.addLayout(newOption)
	config.addCategory(newOption)
	
	n = False
	if not set(oldLayouts) & set(config.layouts):
		print("Error: \n\t Content does not match:\n{}\n{}".format(oldLayouts, config.layouts))
		n = True
	
	if not set(oldCategories) & set(config.categories):
		print("Error: \n\t Content does not match:\n{}\n{}".format(oldCategories, config.categories))
		n = True
		
	if n is True:
		print("Results...\t FAIL")
	else:
		print("Results...\t PASS")	
	
def configBuildTest(location):
	lines()
	print("Testing building a new config file")
	
def testSuite():
	mode = 2

	if mode is 1:
		#config Testing
		configFile = "config"
		configTestOpen(configFile)
		
		# story Testing
		test1 = "testfile.md"
		storyTestContent(test1)
		
		titleTest = "default title for a test"
		storyTestTitle(titleTest)
		# date Testing
		storyTestDate()
		# simple write test in same folder
		writeFileTest(test1, configFile, titleTest)
		# test with a non .md file
		test2 = r'C:\CODEZ\projects\pyJekyllPost\New folder\introPost.txt'
		writeFileTest(test2, configFile, titleTest)

		test3 = r'C:\CODEZ\projects\pyJekyllPost\New folder\msDocTest.docx'
		testTitle3 = "This is the third test"
		#writeFileTest(test3, configFile, testTitle3)
		
	elif mode is 2:	
		test1 = r'C:\CODEZ\projects\pyJekyllPost\New folder'
		configOpen(test1)
		
		test2 = r'C:\CODEZ\projects\pyJekyllPost\New fol'
		configOpen(test2)
	
		newOption = "bananas"
		configAddLayoutCategory(test1, newOption)
		
		configBuildTest(test1)
	
testSuite()