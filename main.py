from threading import Thread, Event
from time import sleep
import indicator
from flask import Flask, render_template
#import Alerts
from queue import Queue
from flask_socketio import SocketIO, emit
from patient import Patient, UnhealthyPatient
import sys

#############################
#
# Main wrapper
#
#
################################

'''
    Example that initializes a healthy patient and prints out vitals.
    Some code in comments that would be for the GUI and alerts. GUI will 
    probably include alerts because we want one place where
    values are being pulled out of the queue and both displayed and analyzed.
    '''

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/', methods=['GET'])
def home():
    try:
        print("Data Starting")
        return render_template('main.html')
    except KeyboardInterrupt:
        print("System Failed, reboot")
        global_kill.set()

pulse_q = Queue()
bp_q = Queue()
bo_q = Queue()

#initialize a healthy patient, with vitals generating every second
patient = Patient(1, pulse_q, bp_q, bo_q)

@socketio.on('stop')
def stop(fakeData):
    global patient
    patient.end_vitals()
    patient = 0
    print("end vitals")

@socketio.on('create')
def startwebApp(fakeData):
    print("got start messages")
    try:
        #start the vitals
        print("starting vitals")
        
        patient.start_vitals()
        #only pulse has a function written
        bp = 0
        bo = 0

        while True:
            pulse = pulse_q.get()
            # bp = bp_q.get()
            # bo = bo_q.get()
            emit('data', {'bp': bp, 'bo': bo, 'pulse': pulse})
            print(pulse)
            sleep(1)
            socketio.sleep(0)

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
#        patient.end_vitals()
 #       sys.exit(1)
    except KeyboardInterrupt:
        print("System Failed, reboot")
        patient.end_vitals()
        global_kill.set()

if __name__ == "__main__":
    socketio.run(app)
