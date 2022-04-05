import RPi.GPIO as GPIO

wait_event=press.Button(10, GPIO.IN, GPIO.PUD_DOWN)
wait_event.setup()
