def healthmon(bp, pulse, boxygen):

	try:
		print("Blood Pressure: " + string(bp))
		print("Pulse: " + string(pulse))
		print("Blood Oxygen: " + string(boxygen))
	except KeyboardInterrupt:
	     print("System Failed, reboot")
	     global_kill.set()
