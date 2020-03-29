from threading import Thread, Event
from time import sleep
from flask import Flask, render_template
import alerts
from queue import Queue
from flask_socketio import SocketIO, emit
from patient import Patient, UnhealthyPatient
import sys

################################
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

pulse_q = Queue()
bp_q = Queue()
bo_q = Queue()

#initialize a healthy patient, with vitals generating every second
patient = Patient(1, pulse_q, bp_q, bo_q)

@socketio.on('stop')
def stop(fakeData):
    #No need to add error check because this kills the program
    global patient
    patient.end_vitals()
    print("end vitals")

@socketio.on('create')
def startwebApp(fakeData):
    try:
        #start the vitals
        print("Starting vitals")
        patient.start_vitals()

        while True:
            pulse = pulse_q.get()
            bp = bp_q.get()
            bo = bo_q.get()

            a = alerts.poll_vitals(pulse, bp, bo)
            emit('alert',{'alert': a }) #sends alert to web app

            emit('data', {'bp0': bp[0], 'bp1': bp[1], 'bo': bo, 'pulse': pulse}) #sends data to web app to display

            sleep(1)
            socketio.sleep(0)


    except KeyboardInterrupt:
        print("System Failed, reboot")
        patient.end_vitals()
        return

if __name__ == "__main__":
    socketio.run(app)
