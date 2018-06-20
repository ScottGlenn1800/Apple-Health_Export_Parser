#Apple Health Export Parser
import re
from optparse import OptionParser

def ParseFilename():
	parser = OptionParser()
	parser.add_option("-f","--file",type="string",dest="filepath",help="The filepath of the export.xml file to parse")
	(options, args) = parser.parse_args()
	file = options.filepath
	return file

def GetEntries(file):
	#Parses through the file and grabs every data entry in the file and adds it to an array.
	Entries = []
	file = ParseFilename()
	with open(file) as Export_File:
		for entry in Export_File:
			if "Record type" in entry:
				Entries.append(entry)
	return Entries

def GetStepEntries(entries):
	#passed a full list of entries
	#Searches a line for the StepCount phrase
	#Get Step Count
	for entry in entries:
		if "StepCount" in entry:
			steps = re.match


def test(file)

def CreateStepExcel
	