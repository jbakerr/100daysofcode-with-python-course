from datetime import datetime
from datetime import timedelta
from time import sleep

active = True
count = 1

while active:
    if count % 3 == 0:
        print("It is time to take a break")
        sleep(10)
        count += 1
    else:
        message = "How long would you like to work? "
        message += "\nPress q to quit "
        timer_length = input(message)
        if timer_length == 'q':
            active = False
        else:
            timer_length = float(int((timer_length)))


            start_time = datetime.today()
            print("Ok, the timer is starting now for " + str(timer_length) + " minutes")
            timer_seconds = timer_length
            count += 1

            sleep(timer_seconds)
            print("Timer Over")





