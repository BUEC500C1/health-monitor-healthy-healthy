from threading import Thread, Event
from time import sleep
#import Alerts

#############################
#
# Main wrapper
#
#
################################

def modify_bp(rate, bp, global_kill):
    while True:
        # bp += some_random_number_thing TODO
        
        if global_kill.is_set():
            break
        
        sleep(1/rate)


global_kill = Event()
warning_event = Event()
emergency_event = Event()

alerts_rate = 1           # Rate of checking for alerts
update_rate = 4           # Update rate of vitals values (Hz)
blood_pressure = 120      # TODO: Write BP function/module (Justin)
blood_oxy = 98            # TODO: Write blood oxygen function/module (Varun)
pulse = 70                # TODO: Write heart rate function/module (Noah)

#  bp_t = Thread(target=bp_module, args=(blood_pressure, rate, ))
#  boxy_t = Thread(target=boxy_module, args=(blood_oxy, rate, ))
#  pulse_t = Thread(target=pulse_module, args=(pulse, rate, ))
#  bp_t.start()
#  boxy_t.start()
#  pulse_t.start()

# alerts = Alerts(warning_event, emergency_event)
while (True):
    try:
        if (warning_event.is_set()):
        print("WARNING!")
        elif (emergency_event.is_set()):
            print("EMERGENCY")

    except KeyboardInterrupt:
        #log_error("Keyboard interrupted monitor")
        global_kill.set()
        break

    sleep(1/alerts_rate)

# bp_t.join()
# boxy_t.join()
# pulse_t.join()