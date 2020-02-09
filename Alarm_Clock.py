#This program rings an alarm according to the user-specified time

import time
import winsound

def intro():
    print("Hello there!")
    print("Welcome to Sleepy Hollow")

    #print current time
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)

    ask1 = input("Would you like to set an alarm? (Y/N): ")
    if ask1 is "Y":
        user_time = input("What time would you like to wake up?(hh:mm:ss format): ")
        return user_time
    elif ask1 is "N":
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(current_time)
    else:
        print("Invalid input")

    t = time.localtime()
    type(t)
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)

#This function calls the alarm when the user-specified time and the actual time
#are the same
#returns boolean
def alarmC (user_time):
    t = time.localtime()
    current = time.strftime("%H:%M:%S", t)
    print(current)
    while True:
        t = time.localtime()
        current = time.strftime("%H:%M:%S", t)
        if current == user_time:
            break
    for i in range (10):
        winsound.Beep(2500,800)
        winsound.Beep(2000,800)
        winsound.Beep(1500,800)
        winsound.Beep(1000,800)

def main():
    user = intro()
    alarmC(user)
main()
