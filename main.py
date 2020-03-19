from threading import Thread, Event
from time import sleep
from queue import Queue

from patient import Patient, UnhealthyPatient

#############################
#
# Main wrapper
#
#
################################

def main():
    '''
    Example that initializes a healthy patient and prints out vitals.
    Some code in comments that would be for the GUI and alerts. GUI will 
    probably include alerts because we want one place where
    values are being pulled out of the queue and both displayed and analyzed.
    '''
    pulse_q = Queue()
    bp_q = Queue()
    bo_q = Queue()

    #initialize a healthy patient, with vitals generating every second
    patient = Patient(1, pulse_q, bp_q, bo_q)

    #start the vitals
    patient.start_vitals()

    #get 10 vitals readings
    count = 10
    while count > 0:
        pulse = pulse_q.get() #only pulse has a function written
        print ("Pulse: ", pulse)
        sleep(1)
        count -= 1

    #instead of the above printing, we'll have:
    # initialize the GUI class
    # health_monitor = HealthMonitor(pulse_q, bp_q, bo_q)
    # 
    # #Launch the GUI along with the alerts system in its own thread
    # health_monitor.launch()
    # From there, database stuff etc?

    # close the GUI after a certain time or from a button press in the GUI 
    # health_monitor.stop()

    #stop generating vitals
    patient.end_vitals()


if __name__ == "__main__":
    main()