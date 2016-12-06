#!/usr/bin/python

import sys
import os
import datetime
import time

def lines():
  print("-------")

def errorMessage(msg, details):
	print("Error: {}.".format(msg))
	print("{}".format(details))
	
	
	
# read in file 
def readFile(filename):
	# try to open the file
	try:
		filedesc = open(filename, 'r')
	except IOError:
		errorMessage("Cannot Open File", "Filename is incorrect or file cannot be read.")
	else: 
		with filedesc as f:
			content = f.read()
		filedesc.close()
		
	return(content)

# add the overhead stuff
def addFrontMatter(contents):
	'''
	---
	layout: post
	title:  "Work Continues"
	date:   2016-12-1 13:52:01 +0900
	categories: story
	---

	'''
	frontMatter = ""
	

	
# discover layout desired

# get date
def getDate():
	# get the current timezone as +-0000
	timezone = int(time.timezone / -(60*60))
	if timezone > 0:
		if timezone > 9:
			timezone = "+" + str(timezone) + "00"
		else:
			timezone = "+" + "0" + str(timezone) + "00"
	else:
		if timezone < -9:
			timezone = "-" + str(timezone) + "00"
		else:
			timezone = "-" + "0" + str(timezone) + "00"	

	print("TIMEZONE {}".format(timezone))
	# time.hour, .minute, .second
	rightNow = datetime.datetime.now()
	today = str(rightNow.date())
	theTime = str(rightNow.hour) + ":" + str(rightNow.minute) + ":" + str(rightNow.second)
	today += " " + theTime + " " + timezone
	return today 

# discover desired categories
def setCategory(filename):
	categories = returnCurrentCategories(filename)

def returnCurrentCategories(filename)

	categories = filename 

	return categories
	
	
	
# discover desired title
def setTitle():
	title = input("Enter the post's title: ")
	return  title 
  
def main():
	if len(sys.argv) < 3:
		errorMessage("Incorrect Input String", "Use: python pyJekyllPost.py [method] [file location]")
	else:
		readFile(sys.argv[2])
# main()