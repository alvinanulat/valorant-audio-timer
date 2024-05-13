from operator import truediv
from PIL import ImageGrab
import time
import keyboard
import voicemeeterlib
import subprocess
KIND_ID = "banana"
vm = voicemeeterlib.api(KIND_ID)
vm.login()

target_x, target_y = 945, 28
deftarget_x, deftarget_y = 416, 49
prev_color1 = (124, 0, 0)
prev_color2 = (170, 0, 0)
f17_pressed= False
vale=True
valf=True
valg=True
scanning_screen="SCANNING"
last_spike_time=0
result_defuse_7sec=0
prev_time=0
spike_7sec=8.33
spike_3sec=4.83
spike_var=spike_7sec
kba=True
script_path = "C:/Users/alvin/Desktop/HOME/2023/PERSONAL_PROJECTS/2023/PROGRAMMING/PY_TESTS/pyvalorantspikecue/text.py"
def current_milli_time():
    return round(time.time() * 1000)

def spike_time():
     return round(float((46-(current_time_ms-prev_time)/1000)),2)
while True:
    if keyboard.is_pressed("F17"):
        f17_pressed = True
    if keyboard.is_pressed("Home"):
            spike_var = spike_7sec
            print("spike time is 7")
    if keyboard.is_pressed("End"):
            spike_var = spike_3sec
            print("spike time is 3")
    # Capture the screen
    screenshot = ImageGrab.grab(bbox=(0, 0, 1920, 1080))  # Adjust 
    # Get the color of the target pixel
    current_color = screenshot.getpixel((target_x, target_y))
#     defcurrent_color = screenshot.getpixel((deftarget_x, deftarget_y))
    last_digits = current_color[1:]
    print(f"{scanning_screen} {current_color} {spike_var} {last_spike_time} {result_defuse_7sec}")
    current_time_ms = current_milli_time()
    # Check if the color has changed
    if (current_color == prev_color1 or current_color == prev_color2) and vale: 
            print(f"SPIKE PLANTED {current_color}")
            vm.apply({"button-32": {"state": True}})
            #keyboard.press_and_release("F15")
            scanning_screen="SPIKE PLANTED"
            prev_time=current_milli_time()
            vale=False
            valf=False
            valg=False
            valh=False
    if last_digits == (0, 0) and valg==False:
        result_defuse_7sec=spike_time()
        if (result_defuse_7sec< spike_var) and valh==False:
                 print("Defusing...")
                 #keyboard.press_and_release("Home")
                 subprocess.Popen(["C:/Program Files/AutoHotkey/AutoHotkey.exe","C:/Users/alvin/Desktop/APPS/TOOLS/MACROS/AHKS/defusespike.ahk"])
                 valh=True
    if last_digits != (0, 0) and valf==False:
       scanning_screen="SCANNING"
       vm.apply({"button-33": {"state": True}})
       last_spike_time=spike_time()
       print(f"Spike time : {last_spike_time}")
       valf=True
       vale=True
       valg=True
    time.sleep(0.01)