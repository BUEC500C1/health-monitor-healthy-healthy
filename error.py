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
    
    
#BLOOD OXYGEN
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

#BP MODULE

def modify_bp(rate, bp, global_kill):
while True:
try:
    bp += random.uniform(-1,1)
    
    except KeyboardInterrupt:
    print("System Failed, reboot")
    global_kill.set()
    break

    # Print statements for testing
    # print("\nBlood pressure is: " + str(bp))
    sleep(1/rate)

#Health indicator
    
def healthmon(bp, pulse, boxygen):

    while (True):
    try:
        print("Blood Pressure: " + string(bp))
        print("Pulse: " + string(pulse))
        print("Blood Oxygen: " + string(boxygen))

    except KeyboardInterrupt:
        print("System Failed, reboot")
        global_kill.set()
        break

#heart_rage

def critical_hr(sig, frame):
    
    while (True):
    try:
        print("Heart is critical")
        #call alarm

    except KeyboardInterrupt:
        print("System Failed, reboot")
        global_kill.set()
        break



def pulse_module(rate, global_kill):
    
        while (True):
        try:
            globals.pulse = random.randint(45, 105)

        except KeyboardInterrupt:
            print("System Failed, reboot")
            global_kill.set()
            break
            sleep(1/rate)

def check_pulse():
    
    while (True):
    try:
        if(globals.pulse <= 49 or globals.pulse >= 101):
            signal.alarm(.05)

    except KeyboardInterrupt:
        print("System Failed, reboot")
        global_kill.set()
        break

#globals

def initilize():
    
    while (True):
    try:
        global pulse
        pulse = 70

    except KeyboardInterrupt:
        print("System Failed, reboot")
        global_kill.set()
        break
    
    

