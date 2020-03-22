while (True):
try:
    if (warning_event.is_set()):
    print("WARNING!")
    elif (emergency_event.is_set()):
        print("EMERGENCY")

except KeyboardInterrupt:
    #log_error("Keyboard interrupted monitor")
    global_kill.set()
    break
