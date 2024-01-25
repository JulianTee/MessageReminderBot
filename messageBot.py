from datetime import date
from twilio.rest import Client
from credentials import twilio_num, account_sid, auth_token, phoneNums

client = Client(account_sid, auth_token)
client.edge = 'ashburn'

file = open('INSERT FILE PATH HERE E.G. C:/Users/John/weekCount.txt', 'r+') # opens the file that contains week count
data = file.read()
currWeek = int(data)  # currWeek is the week count that determines whose turn it is 0-3

note = open('INSERT FILE PATH HERE E.G. C:/Users/John/msgCount.txt', 'r+')# opens text file containing message count
info = note.read()
count = int(info)

todayDate = date.today()


first_reminder = "Hi! Today is your turn for Trash Day! Please remember to take out the trash and replace the bag! "
second_reminder = "Reminder: Don't forget to take out the trash! "


def week_increment(val):
    "increments week and resets to 0 if it has been 4 weeks"
    if currWeek == 4:
        "if week 4 set val to -1 so final sum is 0 (resets the count)"
        val = -1
    file.seek(0)
    file.write(str(val+1))
    file.truncate()


def message_tracker(num):
    "keeps track of how many messages were sent today"
    if count == 1:
        num = -1
    note.seek(0)
    note.write(str(num+1))
    note.truncate()


def create_message(curr_phone, reminder):
    "function that creates a message"
    message = client.messages.create(to=curr_phone,from_=twilio_num,
            body=reminder)
    print(message.sid)


if todayDate.weekday() == 0:  # checks if the day is monday (day 0)
    if currWeek == 0:   # assigns the right phone number to curr_phone (depending on the list order in credentials.py)
        curr_phone = phoneNums[0]
    elif currWeek == 1:
        curr_phone = phoneNums[1]
    elif currWeek == 2:
        curr_phone = phoneNums[2]
    elif currWeek == 3:
        curr_phone = phoneNums[3]

    if count == 0:
        "if the number of messages sent today == 0, message_tracker will send the first reminder "
        create_message(curr_phone, first_reminder)
        message_tracker(count)
    elif count == 1:
        "else the second reminder will be sent "
        create_message(curr_phone, second_reminder)
        message_tracker(count)
        week_increment(currWeek)




