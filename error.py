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
    
    
    
    def critical_blood_oxy(sig, frame):
    while (True):
    try:
        print("Blood Oxygen is at a critical point")

    except KeyboardInterrupt:
        print("System Failed, reboot")
        global_kill.set()
        break
        
        #call alarm



    def bloodOxygen_module(rate, global_kill):
        
        while True:
        try:
            globals.blood_oxy = random.randint(95, 99)

        except KeyboardInterrupt:
            print("System Failed, reboot")
            global_kill.set()
            break
          
            sleep(1/rate)

    def check_blood_oxy():
    
    while True:
    try:
        if(globals.blood_oxy <= 94):
            signal.alarm(.05)

    except KeyboardInterrupt:
        print("System Failed, reboot")
        global_kill.set()
        break
        

