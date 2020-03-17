import random
from random import randint
from time import sleep

def pulse_module(rate, pulse, global_kill):
 
    while True:
        pulse = random.randint(45, 105)
    
        if (pulse >= 101 or pulse <= 49):
            #alert
            print("help")

        if global_kill.is_set():
            break
      
        sleep(1/rate)






