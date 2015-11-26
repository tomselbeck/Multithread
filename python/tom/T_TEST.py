import sched
import time

currentTime = time.asctime()

print currentTime[11:16]


while currentTime[11:16] != "16:21":
	currentTime = time.asctime()
	print currentTime[11:16]	
	time.sleep(1)
	pass




