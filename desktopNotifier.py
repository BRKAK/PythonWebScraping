from datetime import datetime
import win10toast
import time
from win10toast import ToastNotifier
def currentTimerCounter():
    now=datetime.now()
    currTime=now.strftime("%H:%M:%S")
    print("\n------------------------------\nCurrent Time:",currTime,"\n------------------------------\n")

def showToast(msg):
    toaster = ToastNotifier()
    toaster.show_toast(
    msg=msg,
    title="ZA XD CORP.",
    icon_path=None,
    duration=5,
    threaded=True)
def alarmCallBack(counter):
    msg=(str)(counter)+" seconds has passed!"
    showToast(msg)
    
    #now=datetime.now()
    #minute=now.minute
    #print("\nMinute: ", minute)
    #print("Alarm!!!\n5 seconds has passed!")
    
counter = 0

while True:
    if counter % 10 == 0 and counter != 0:
        alarmCallBack(counter)
    currentTimerCounter()
    time.sleep(1)
    counter+=1
    

    


    