##Imported libraries
import time
from gpiozero import LED, Button

##Push buttons with pins
redPushbutton = Button (17)
greenPushbutton = Button (27)
bluePushbutton = Button (22)

#LED's with pins
redLed = LED (26)
greenLed = LED (19)
blueLed = LED (13)

#While loop 
while True:
    
    ##If Statements
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

    