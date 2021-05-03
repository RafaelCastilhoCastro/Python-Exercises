from playsound import playsound

import time

hour = "11"
minut = "45"
secs = "00"
alarm = hour+":"+minut+":"+secs
alarm_end = hour+":"+minut+":"+"15"

while True:
	print("\n"*100)
	print(time.strftime("%X"))
	time.sleep(1)
	if time.strftime("%X") == alarm:
			playsound("alarm.mp3",False)	# False causa execução do som assincronicamente, então o relógio prossegue.
		


