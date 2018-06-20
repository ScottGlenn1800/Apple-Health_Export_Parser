#Apple Health Export Parser Classes

class StepCountRecord(object):
	'''This class defines the attributes of the
	   Apple Health Export xml file supplied to 
	   the class. i.e. how many steps were recorded,
	   What date were the steps recorded, what time
	   did the recording start, and what time did the 
	   recording end.'''
	def __init__ (self,steps,date,starttime,endtime):
		self.steps=steps
		self.date=date
		self.starttime=starttime
		self.endtime=endtime