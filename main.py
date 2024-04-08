#ShutApp, A simple python program the blocks programs to help you focus

from tkinter import *
import subprocess
import time

root = Tk()
root.title('ShutApp')
root.overrideredirect(False)
root.geometry("220x100")
root.resizable(width=False, height=False)
bg=PhotoImage(file="shutapp2.png")
bgLabel = Label(root,image=bg)
bgLabel.place(x=-20,y=-50)

timeout = time.time()
settime = 0 # time in seconds, this is what the actual timer uses
timeInH = 0 #time in hours for easier use, actual timer does not use this value
timeblocked = 0

clickStart = False
clickSub = False

print("Please input the software you want to block:")
print("example: firefox.exe")
#takes users input and passes it through string command that will be ran in killProccess()
userInput = input()
taskToKill = f"TASKKILL /F /IM {userInput}"

#printing what the time is set to
print("Time:", timeInH,"h","||",settime,"s")
def ClickStart():
    global clickstart
    global timeout
    global settime
    global startButton
    if clickStart == False:
        root.overrideredirect(True)
        timeout = time.time() + settime  # sets the time to end killProcess loop to whatever user set
        root.after(1000, killProcess)
        myLabel = Label(root, text="Blocking started").pack()
        print("Blocking Started")
        startButton = DISABLED
        clickstart = True

def clickSub():
    global settime
    global timeInH
    if settime > 0:
        settime = settime - 3600
        timeInH = timeInH - 1

        print("Time:", timeInH,"h","||",settime,"s")
    elif settime <= 0 & timeInH <= 0:
        print("Cannot set time lower than 0")


def clickAdd():
    global settime
    global timeInH
    settime = settime + 3600
    timeInH = timeInH + 1

    print("Time:", timeInH,"h","||",settime,"s")


startButton = Button(root, text="Start Blocking", command=ClickStart, bg="LightGreen")
startButton.pack()

subTimeButton = Button(root, text="Subtract Hour", command=clickSub)
subTimeButton.pack()

addTimeButton = Button(root, text="Add Hour",command=clickAdd)
addTimeButton.pack()


# infinite loop that kills process
def killProcess():
    global timeblocked
    # checking if current time is less than the time to stop, if it is keep going
    if time.time() < timeout:
        print(timeblocked)
        subprocess.call(taskToKill, shell=False) #kills the task user set
        root.after(600, killProcess)
        timeblocked = timeblocked + 1

root.mainloop()