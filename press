import RPi.GPIO as GPIO

class button:
    def __init__(self, pin, inout, updown):
        self.pin = pin
        self.inout = inout
        self.updown = updown

    
    
    def setup(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, self.inout, pull_up_down=self.updown)
        
        #GPIO.PUD_UP
        #GPIO.PUD_DOWN
        #GPIO.IN
