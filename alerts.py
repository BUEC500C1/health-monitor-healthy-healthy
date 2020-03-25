# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

def poll_vitals(pulse, bp, bo):
    '''
    Check the values of the vitals of the patient.
    Return a string indicating the alert, else ""
    '''
    return ""
    

def sendemail(alertMsg, subject):
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
