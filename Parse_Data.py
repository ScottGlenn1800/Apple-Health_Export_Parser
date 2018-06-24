#Apple Health Export Parser
import re,sys,openpyxl,os,distutils.dir_util
from optparse import OptionParser
sys.path.append("C:\CODE\Apple_Health_Export_Parser")
from Record_Classes import *

def ParseFilename():
	parser = OptionParser()
	parser.add_option("-f","--file",type="string",dest="filepath",help="The filepath of the export.xml file to parse")
	(options, args) = parser.parse_args()
	file = options.filepath
	if options.filepath==None:
		print"Error! Please enter the filepath of the export file."
		sys.exit()
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

def GetStepRecords(entries):
	#passed a full list of entries
	#Searches a line for the StepCount phrase
	#Get Step Count
	StepRecords = []
	for entry in entries:
		if "StepCount" in entry:
			#gets the amount of steps out of the entry
			steps = re.search(r'value="[0-9]+"',entry)
			steps = re.search(r'[0-9]+',steps.group(0))
			steps = steps.group(0)
			#Gets the date out of the entry (YYYY-MM-DD)
			date = re.search(r'[0-9]{4}-[0-9]{2}-[0-9]{2}',entry)
			date = date.group(0)
			#Gets the start and end times
			times = re.findall(r'[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}',entry)
			del times[0] #The first time in the record is the record creation date, (doesn't happen at time of event) so it gets deleted
			starttime = times[0]
			endtime = times[1]
			record = StepCountRecord(steps,date,starttime,endtime)
			StepRecords.append(record)
	return StepRecords

def CreateStepExcel(StepRecords):
	distutils.dir_util.mkpath() #Creates the Directory. 
	Sheet = openpyxl.Workbook()


file = ParseFilename()
entries = GetEntries(file)
StepRecords = GetStepRecords(entries)
for record in StepRecords:
	print record.starttime
print len(StepRecords)

	