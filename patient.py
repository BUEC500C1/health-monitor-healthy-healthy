from threading import Thread, Event
import queue
import random
from time import sleep

class Patient(Object):
    '''
    A class that mimics a patient's vitals, and pushes blood pressure, blood
    oxygen, and pulse data to the queues that are provided as arguments
    The constructor takes the following inputs:
        1) Pulse queue
        2) Blood pressure queue
        3) Blood Oxygen queue
    '''

    def __init__(self, update_rate, pulse_q, bp_q, bo_q):
        self.rate = update_rate                  #Defines the rate of vitals data generation

        # This parent class defaults to a healthy patient, see gen functions for healthy behavior
        self.prev_pulse = 70
        #self.prev_bp = (120, 80) #initial blood pressure is healthy
        #self.prev_bo = 98 #initial blood oxygen is healthy

        # Load vitals data buffers
        self.pulse_q = pulse_q
        self.bp_q = bp_q
        self.bo_q = bo_q

        # Kill switch
        self.end = 0

    def start_vitals(self):
        '''Launch the vitals generators in multiple threads'''
        pulse_thread = Thread(target=self.pulse_gen, args=(self.pulse_q,))
        #bp_thread = Thread(target=self.bp, args=(self.bp_q,))
        #bo_thread = Thread(target=self.bo, args=(self.bo_q,))
        
        pulse_thread.start()
        #bp_thread.start()
        #bo_thread.start()

        while not self.end:         #Temporary, read and print the vitals to std out every second
            p = self.pulse_q.get()
            print("Pulse: ", p)
            sleep(1)
        pulse_thread.join()
        
    def pulse_gen(self, q):
        '''Generate a healthy pulse, that varies uniformly around initial value'''
        while not self.end:
            pulse = self.prev_pulse + random.uniform(-1, 1)
            q.put(pulse)
            self.prev_pulse = pulse
            sleep(int(1/self.rate))
        return

    def bp_gen(self, q): # TODO, write for a healthy patient as the default for the parent class
        return (120,8)
    def bo_gen(self, q): # TODO, write for a healthy patient as the default for the parent class
        return 98

    def end_vitals(self):
        self.end = 1


class UnhealthyPatient(Patient):
    def __init__(self, update_rate, pulse_q, bp_q, bo_q)):
        super(UnhealthyPatient, self).__init__(update_rate, pulse_q, bp_q, bo_q))
        
        #for init, everything else is the same as the parent except the starting vitals
        self.prev_pulse = 100 #initial pulse is high
        #self.prev_bp = (130, 90) #initial blood pressure is high
        #self.prev_bo = 95 #initial blood oxygen is lower

    def pulse_gen(self, q):
        return 100 #TODO: override parent generator, write for an unhealthy patient
    
    def bp_gen(self, q):
        return (130, 90) #TODO: override parent generator, write for an unhealthy patient

    def bo_gen(self, q):
        return 95 #TODO: override parent generator, write for an unhealthy patient