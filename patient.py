from threading import Thread, Event
import queue
import random
from time import sleep

class Patient():
    '''
    A class that mimics a patient's vitals, and pushes blood pressure, blood
    oxygen, and pulse data to the queues that are provided as arguments
    The constructor takes the following inputs:
        1) Pulse queue
        2) Blood pressure queue
        3) Blood Oxygen queue
    '''
    def __init__(self, update_rate, pulse_q, bp_q, bo_q):
        try:
            self.rate = update_rate                       # Defines the rate of vitals data generation

            # This parent class defaults to a healthy patient, see gen functions for healthy behavior
            self.prev_pulse = random.randint(60, 80)
            self.prev_systolic = random.randint(115, 120) # Initial blood pressure is healthy
            self.prev_diastolic = random.randint(75,80)   # (120, 80) = (systolic, diastolic)
            self.prev_bo = random.randint(95, 98)         # Initial blood oxygen is healthy

            # Load vitals data buffers
            self.pulse_q = pulse_q
            self.bp_q = bp_q
            self.bo_q = bo_q

            # Kill switch
            self.end = 0
        except KeyboardInterrupt:
            print("System Failed, reboot")
            return 

    def start_vitals(self):
        try:
            '''Launch the vitals generators in multiple threads'''
            pulse_thread = Thread(target=self.pulse_gen, args=(self.pulse_q,))
            bp_thread = Thread(target=self.bp_gen, args=(self.bp_q,))
            bo_thread = Thread(target=self.bo_gen, args=(self.bo_q,))
            
            pulse_thread.start()
            bp_thread.start()
            bo_thread.start()
        except KeyboardInterrupt:
            print("System Failed, reboot")
            return
        
    def pulse_gen(self, q):
        '''Generate a healthy pulse, that varies uniformly around initial value'''
        try:
            while not self.end:
                pulse = round(self.prev_pulse + random.uniform(-1, 1), 1)
                q.put(pulse)
                self.prev_pulse = pulse
                sleep(int(1/self.rate))
            return
        except KeyboardInterrupt:
            print("System Failed, reboot")
            return

    def bp_gen(self, q):
        '''Generate healthy blood pressure readings and put a tuple in the queue''' 
        try:
            while not self.end:
                systolic = round(self.prev_systolic + random.uniform(-1,1), 1)
                diastolic = round(self.prev_diastolic + random.uniform(-1,1), 1)
                bp = (systolic, diastolic)
                q.put(bp)
                self.prev_systolic = systolic
                self.prev_diastolic = diastolic
                sleep(int(1/self.rate))
            return
        except KeyboardInterrupt:
            print("System Failed, reboot")
            return
        
    def bo_gen(self, q):
        '''Generate values for healthy blood oxygen'''
        try:
            self.prev_bo = random.randint(95, 99)
            while not self.end:
                bo = self.prev_bo + random.randint(-2, 2)
                if (bo > 100):
                    bo = 99
                q.put(bo)
                self.prev_bo = bo
                sleep(int(1/self.rate))
            return
        except KeyboardInterrupt:
            print("System Failed, reboot")
            return

    def end_vitals(self):
        try:
            self.end = 1
        except KeyboardInterrupt:
            print("System Failed, reboot")
            return
        
class UnhealthyPatient (Patient):
    '''
    Unhealthy Patient class that generates unhealthy values for the patient's vitals.
    This is to test the alerts functionality of the software.
    '''
    def __init__(self, update_rate, pulse_q, bp_q, bo_q):
        try:
            super(UnhealthyPatient, self).__init__(update_rate, pulse_q, bp_q, bo_q)
            
            #for init, everything else is the same as the parent except the starting vitals
            self.prev_pulse = 100      #initial pulse is high
            self.prev_bp = (130, 90)   #initial blood pressure is high
            self.prev_bo = 95          #initial blood oxygen is lower
        except KeyboardInterrupt:
            print("System Failed, reboot")
            return
        
    def pulse_gen(self, q):
        try:
            bad_value = 0
            while not self.end:
                bad_value = random.randint(0, 6)
                if (bad_value == 5):
                    pulse = random.randint(40, 59)
                else:
                    pulse = round(self.prev_pulse + random.uniform(-2, 2), 1)
                q.put(pulse)
                self.prev_pulse = pulse
                sleep(int(1/self.rate))
                return
        except KeyboardInterrupt:
            print("System Failed, reboot")
            return
         
    def bp_gen(self, q):
        '''Generate aggressively changing blood pressure values, put tuple in queue'''
        try:
            while not self.end:
                systolic = round(self.prev_systolic + random.uniform(-4,4), 1)
                diastolic = round(self.prev_diastolic + random.uniform(-4,4), 1)
                bp = (systolic, diastolic)
                q.put(bp)
                self.prev_systolic = systolic
                self.prev_diastolic = diastolic
                sleep(int(1/self.rate)) 
        except KeyboardInterrupt:
            print("System Failed, reboot")
            return
        
    def bo_gen(self, q):
        try:
            while not self.end:
                bo = self.prev_bo + random.randint(-2, 2)
                if (bo > 100):
                    bo = 99
                q.put(bo)
                self.prev_bo = bo
                sleep(int(1/self.rate))
                return
        except KeyboardInterrupt:
            print("System Failed, reboot")
            return
