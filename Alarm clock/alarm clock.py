from playsound import playsound

import time

hour = "11"
minute = "45"
secs = "00"
alarm = hour+":"+minute+":"+secs
alarm_end = hour+":"+minute+":"+"15"

while True:
	print("\n"*100)
	print(time.strftime("%X"))
	time.sleep(1)
	if time.strftime("%X") == alarm:
			playsound("alarm.mp3",False)	# False causa execução do som assincronicamente, então o relógio prossegue.
