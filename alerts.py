from threading import Thread, Event
from time import sleep

#################################################
#
# Alerts module for wrapping all of alerts 
#  functionality.
# Copyright Healthy Healthy Hippos, Jacob Davis
#
#################################################

class Alerts():
    def __init__(self, rate, emergency_event, warning_event):
        self.rate = rate
        self.emergency = alarm_event
        self.warning = warning_event

    def monitor_bp(self, bp):
        # Monitor blood pressure
        # Input in the form of a tuple (systolic, diastolic)
        while (True):
            if ((bp[0] > 180) or (bp[1] > 120)): # emergency
                self.emergency.set() #set the emergency alarm

            elif ((bp[0] > 130) or (bp[1] > 80)): # warning
                self.warning.set()   #set the warning alarm

            sleep(int(1/self.rate))

    def monitor_pulse(self, pulse):
        # Monitor the pulse 
        # Input in form of integer BPM
        while (True):
            if ((pulse > 135) or (pulse < 45)): # emergency
                self.emergency.set() #set the emergency alarm
                
            elif ((pulse > 145) or (pulse < 35)): # warning
                self.warning.set()   #set the warning alarm

            sleep(int(1/self.rate))

    def monitor_ox(self, bo)
        # Monitor the blood oxygen 
        # Input provided as an integer percentage
        while (True):


            sleep(int(1/self.rate))

