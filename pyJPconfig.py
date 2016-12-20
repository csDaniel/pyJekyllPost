#!/usr/bin/python

import sys
import os
import glob

from pyJekyllPost import lines
from pyJekyllPost import errorMessage

# this is going to let us set config stuff!

class Config(object):
	def __init__(self):
		self.location = None
		self.categories = []
		self.layouts = []
		
	def setConfig(self):
		self.location = self.getLoc(submittedLocation)

	def getLoc(self, submittedLocation):
		if os.path.exists(submittedLocation):
			location = glob.glob(submittedLocation + '\*')
			self.location = submittedLocation
			
			for story in location:
				#print("{}".format(story))
				self.getMetaData(story)		
			
			#attempt to read the directory found at submittedLocation
		else:
			errorMessage("Incorrect File Location", "\'{}\' cannot be opened.".format(submittedLocation))
		
	def getMetaData(self, inputFile):
		try:
			filedesc = open(inputFile, 'r')
		except IOError:
			errorMessage("Cannot Open File", "Filename is incorrect or file cannot be read.")
		else:
			for line in filedesc:
				line = line.rstrip()
				#print("{}".format(line))
				if "layout:" in line:
					chunks = line.split(": ")
					if chunks[1] not in self.layouts:
						self.layouts.append(chunks[1])
				if "categories:" in line:
					chunks = line.split(": ")
					if chunks[1] not in self.categories:
						self.categories.append(chunks[1])
			filedesc.close()
		# from the loc, scan files for "layout" tag
	
	def addLayout(self, newLayout):
		# add a new layout based on user input.
		self.layouts.append(newLayout)
	
	def addCategory(self, newCategory):
		self.categories.append(newCategory)
	
	def buildConfig(self):
		configString = "loc=" + self.location + "$#layouts=" + str(self.layouts) + "$#categories=" + str(self.categories)
		# loc=C:\CODEZ\projects\pyJekyllPost\New folder$#layouts=default,post$#categories=code,story
		
		
		
		
		
		
		
		
		