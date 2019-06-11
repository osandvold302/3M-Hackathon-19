import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print "Button Pressed"
        time.sleep(10)  # sleep for 10 seconds before allowing another press
