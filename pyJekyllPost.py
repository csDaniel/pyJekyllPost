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
	
	
	
	
class Story(object):	
	def __init__(self):
		#config = configOpen(configFile)
		self.date = None 
		self.title = None
		self.location = None
		self.layouts = []
		self.categories = []
		self.content = None

	# discover desired title
	def setTitle(self, title):
		self.title = title

	# get date
	def setDate(self):
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

		rightNow = datetime.datetime.now()
		today = str(rightNow.date())
		theTime = str(rightNow.hour) + ":" + str(rightNow.minute) + ":" + str(rightNow.second)
		today += " " + theTime + " " + timezone

		self.date =  today 
		
	# config stuff. maybe move to seperate file?
	def configOpen(self, configFile):
		try:
			filedesc = open(configFile, 'r')
		except IOError:
			errorMessage("Cannot Open Config", "Config File cannot be Located")
			noConfigAnswer = input("Would you like to make a new Config File? y/n \n")
			noConfigAnswer.lower()
			if noConfigAnswer[0] is "y":
				makeNewConfig()
			else:
				errorMessage("Goodbye","pyJekyll cannot operate without a config file.")
		else:
			# config file is located
			configRaw = filedesc.read()
			configRaw = configRaw.split("$#")
			config = self.formatConfigDataFromFile(configRaw)
			
			# set the class stuff
			self.location = config.outputLocation
			self.layouts = config.layouts
			self.categories = config.categories 

	def formatConfigDataFromFile(self, fileContents):
		configDict = {}
		configDict['layouts'] = {}
		configDict['categories'] = {}

		for eachLine in fileContents:
			chunks = eachLine.split("=")
			if chunks[0] == 'loc':
				configDict['location'] = chunks[1]
			if chunks[0] == "layouts":
				configDict['layouts'] = chunks[1].split(",")
			if chunks[0] == "categories":
				configDict['categories'] = chunks[1].split(",")
		
		class Config(object):
			def __init__(self):
				self.outputLocation = configDict['location']
				self.layouts = configDict['layouts']
				self.categories = configDict['categories']
		
		config = Config()
		return config	
		
	def getContent(self, filename):
		try:
			filedesc = open(filename, 'r')
		except IOError:
			errorMessage("Cannot Open File", "Filename is incorrect or file cannot be read.")
		else: 
			with filedesc as f:
				content = f.read()
			filedesc.close()		
		self.content = content
		#return(content)
		
	def saveStory(self, filename):
		filename = self.title.replace(" ", "-")
		filename = self.location +"/" + filename
		try:
			fileDesc = open(filename, 'w')
		except IOError:
			print("Error: could not write to file {}".format(filename))
		else:
			post = "--- \nlayout: " + self.layouts[1] + "\n"
			post = post+ "title: \"" + self.title + "\"\n"
			post = post+ "date: " + self.date + "\n"
			post = post+ "categories: " + self.categories[1] + "\n---\n\n"
			post = post+ self.content + "\n"			
			fileDesc.write(post)
			fileDesc.close()
	

def makeNewConfig():
	print("WE DID IT")
# discover layout desired

	
def main():
	if len(sys.argv) < 3:
		errorMessage("Incorrect Input String", "Use: python pyJekyllPost.py [method] [file location]")
	else:
		readFile(sys.argv[2])
# main()