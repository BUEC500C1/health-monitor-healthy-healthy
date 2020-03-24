import random
from time import sleep

# Takes in a rate (reads/second), an initialized bp, and a global_kill event
def modify_bp(rate, bp, global_kill):
    while True:
        try:
            bp += random.uniform(-1,1)
        
            except KeyboardInterrupt:
                print("System Failed, reboot")
                global_kill.is_set():
                break

            # Print statements for testing
            # print("\nBlood pressure is: " + str(bp))
            sleep(1/rate)
        
        
        
        

