# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

def poll_vitals(pulse, bp, bo):
    try:
        
        '''
        Check the values of the vitals of the patient.
        Return a string indicating the alert, else ""
        '''
        alert_string = ""
        only_alert = True   #for formatting
        if (pulse > 120):
            only_alert = False
            alert_string += "Pulse is abnormally high"
        
        if (pulse < 50):
            if (only_alert):
                alert_string += "Pulse is abnormally low"
                only_alert = False
            else:
                alert_string += "; Pulse is abnormally low"
        
        if (bp[0] > 160 or bp[1] > 90):
            if (only_alert):
                alert_string += "Blood pressure is abnormally high"
                only_alert = False
            else:
                alert_string += "; Blood pressure is abnormally high"

        if (bp[0] < 90 or bp[1] < 70):
            if (only_alert):
                alert_string += "Blood pressure is abnormally low"
            else:
                alert_string += "; Blood pressure is abnormally low"

        if (bo < 94):
            if (only_alert):
                alert_string += "Blood oxygen is abnormally low"
            else:
                alert_string += "; Blood oxygen is abnormally low"
        return alert_string
    except KeyboardInterrupt:
        print("System Failed, reboot")
        patient.end_vitals()
        return

def sendemail(alertMsg, subject):
    try:
        msg = EmailMessage()
        msg.set_content(str(alertMsg))

        from_addr = 'healthyhealthyhippos@gmail.com'
        to_addr_list = ['justinfm@bu.edu']

        msg['Subject'] = 'Important Health Monitor Alert Regarding: ' + str(subject)
        msg['From'] = from_addr
        msg['To'] = ','.join(to_addr_list)

        login = "healthyhealthyhippos"
        password = "thehealthiesthippos"
        smtpserver='smtp.gmail.com:587'

        server = smtplib.SMTP(smtpserver)
        server.connect("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(login,password)
        problems = server.send_message(msg)
        server.quit()
    except:
        print("System Failed, reboot")
        patient.end_vitals()
        return
