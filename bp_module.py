import random
from time import sleep

def modify_bp(rate, bp, global_kill):
    while True:
        bp += random.uniform(-1,1)
        # if global_kill.is_set():
        #     break
        print("\nBlood pressure is: " + str(bp))
        sleep(1/rate)