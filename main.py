import pywhatkit
import datetime
import random
from contacts_list import get_number
from generate_msg import generate_msg

contact_name = input('Enter contact name ').title()
if contact_name == "Lundi": 
    print("Generating message for Lundi")
    msg = generate_msg()
else:
    msg = input("Enter message ")
    print("Message generated")

contact_number = get_number(contact_name)

time_dialtion = input("Send message now? ")
if time_dialtion == "Yes" or "yes" or "y" or "Y":
    time = datetime.datetime.now()
    hour = time.hour
    minute = time.minute + 1
else:
    hour1 = int(input("Send message between __ o'clock" ))
    hour2 = int(input("and __ o'clock "))
    hour = random.randint(hour1, hour2)
    minute = random.randint(0, 59)
    print(f"your message will be sent at {hour}:{minute}")


pywhatkit.sendwhatmsg(contact_number, msg, hour, minute, wait_time= 15, tab_close=True)