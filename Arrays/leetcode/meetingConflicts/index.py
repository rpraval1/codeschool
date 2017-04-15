"""
:Author: Pravallika
:Description: Detect conflict in meeting schedules
"""

class Schedule(object):
	def __init__(self, roomId, hour, min):
		self.roomId = roomId
		self.hour = hour
		self.min = min
	
	def __str__(self):
		return "Room: %d is booked for %d:%d" % (self.roomId, self.hour, self.min)


class Meeting(object):
	def checkConflict(self, schedules, input):
		"""
		:type schedules: List(Schedule)
		:type input: Schedule
		:rtype: bool
		"""
		
		print("Current Schedule: ")
		booked = False

		for i in range(len(schedules)):
			print(schedules[i])
			if (schedules[i].roomId == input.roomId) and (schedules[i].hour == input.hour) and (schedules[i].min == input.min):
				booked = True
		if(booked):
			print("Conflict detected for requested meeting room: "+ str(input.roomId)+" at "+str(input.hour)+":"+str(input.min))
		else:
			print("Meeting room: "+ str(input.roomId)+" at "+str(input.hour)+":"+str(input.min)+" is available")

		return booked


schedule1 = Schedule(1,9,0)
schedule2 = Schedule(1,10,0)
schedule3 = Schedule(2,11,30)

schedules = []
schedules.append(schedule1)
schedules.append(schedule2)
schedules.append(schedule3)

inputSchedule = Schedule(1,10,0)
meeting = Meeting()
print(meeting.checkConflict(schedules,inputSchedule))

inputSchedule = Schedule(1,13,30)
meeting = Meeting()
print(meeting.checkConflict(schedules,inputSchedule))
