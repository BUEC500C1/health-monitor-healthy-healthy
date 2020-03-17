import random
from random import randint
from time import sleep
import signal
import globals
import os


def critical_hr(sig, frame):
    print("Heart is critical")
    #call alarm



def pulse_module(rate, global_kill):
    
    while True:
        globals.pulse = random.randint(45, 105)

        if global_kill.is_set():
            break
      
        sleep(1/rate)

def check_pulse():
    if(globals.pulse <= 49 or globals.pulse >= 101):
        signal.alarm(.05)




