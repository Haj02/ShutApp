# This program will try to close a specfied window every second
# Using subprocess to fetch the process we wanna kill

from tkinter import *
import subprocess
import time

root = Tk()
root.title('ShutApp')
root.overrideredirect(False)
root.geometry("220x100")
root.iconbitmap('shutappicon.ico')
root.resizable(width=False, height=False)

clickstart = False
runloop = False
timeout = time.time()
settime = 10 # time in seconds
timeblocked = 0

def ClickStart():
    global clickstart
    global runloop
    global timeout
    global settime
    if clickstart == False:
        root.overrideredirect(True)
        timeout = time.time() + settime  # sets the time to end killProcess loop to whatever user set
        root.after(1000, killProcess)
        myLabel = Label(root, text="Blocking started").pack()
        clickstart = True

startButton = Button(root, text="Start Blocking", command=ClickStart, bg="LightGreen")
startButton.pack()

# infinite loop that kill process
def killProcess():
    global timeblocked
    # checking if current time is less than the time to stop, if it is keep going
    if time.time() < timeout:
        print(timeblocked)
        subprocess.call("TASKKILL /F /IM brave.exe", shell=False)
        root.after(600, killProcess)
        timeblocked = timeblocked + 1

root.mainloop()


