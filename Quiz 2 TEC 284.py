import time
from gpiozero import LED, Button

redPushbutton = Button (17)
greenPushbutton = Button (27)
bluePushbutton = Button (22)

redLed = LED (26)
greenLed = LED (19)
blueLed = LED (13)
while True:
    
    if redPushbutton.is_pressed:
    
        redLed.on()
    
        time.sleep(1)
    
    else:
        redLed.off()
        
    if greenPushbutton.is_pressed:
    
        greenLed.on()
    
        time.sleep(1)
    
    else:
        greenLed.off()
        
    if bluePushbutton.is_pressed:
    
        blueLed.on()
    
        time.sleep(1)
    
    else:
        blueLed.off()

    