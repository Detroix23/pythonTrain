import keyboard
from pynput import Controller
import time

mouse = Controller()
cooldown = 0.000000000000000000001
# /!\ Si vous mettez le "cooldown" a 0, votre fenêtre ouverte risque de crasher /!\ 

while True:
        if keyboard.is_pressed('f'):
                while not keyboard.is_pressed('v'):
                        mouse.click(Button.right, 1)    #droite
                        time.sleep(cooldown)


    

    
    
    
