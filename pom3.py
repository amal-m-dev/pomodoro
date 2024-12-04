from guizero import App, Text, Box, TitleBox, PushButton, Picture
import winsound
# import notif

import time

global minute, second
minute = 24
second = 59


global paused
paused = False

def counter():
    if paused:
        return
    if int(minutes.value) == 0 and int(seconds.value) == 0:
        for i in range(3):
            winsound.Beep(500, 500)
            time.sleep(0.5)
        
        reset_counter()
        
    else:
        if int(seconds.value) == 0:
            seconds.value = f"{str(second)}"
            minutes.value = str(int(minutes.value) - 1)
        else:
            seconds.value = str(int(seconds.value) - 1)

def start_or_pause_counter():
    if button.text == "Start":
        button.text = "Pause"
        paused = False
        app.repeat(1000, counter)  # Schedule counter to be called every 1000ms
    else:
        button.text = "Start"
        paused = True
        app.cancel(counter)  # Cancel the scheduled call to counter

def reset_counter():
    minutes.value = f"{str(minute)}"
    seconds.value = f"{str(second)}"
    button.text = "Start"
    if paused == False:
        app.cancel(counter)

app = App("Pomodoro Timer", width=400, height=200, bg="black", layout="grid")
pic = Picture(app, image="pom.png", grid=[0,0])
box = Box(app, layout="grid", grid=[3,0])
buttonBox = Box(app, grid=[3,2])


minutes = Text(box, text=f"{str(minute)}", align="top", bg="black", color="white", grid=[0,0])
Text(box, text=":", align="top", bg="black", color="white", grid=[1,0])
seconds = Text(box, text=f"{str(second)}",align="top", bg="black", color="white", grid=[2,0])
button = PushButton(buttonBox, text="Start", command=start_or_pause_counter)
reset_button = PushButton(app, text="Reset", command=reset_counter, grid=[4,2])
reset_button.bg = "red"
button.text_color = "white"

app.display()