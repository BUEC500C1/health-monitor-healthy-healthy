while (True):
try:
    if (warning_event.is_set()):
    print("WARNING!")
    elif (emergency_event.is_set()):
        print("EMERGENCY")

except KeyboardInterrupt:
    print("System Failed, reboot")
    global_kill.set()
    break
