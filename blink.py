import RPi.GPIO as GPIO 
import time

led1 = 7
led2 = 29
led3 = 8
led4 = 10

led = [led1, led2, led3, led4]

GPIO.setmode(GPIO.BOARD)
for i in led:
    GPIO.setup(i, GPIO.OUT)

for k in range(5):
    for j in led:
        GPIO.output(j,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(j,GPIO.LOW)
        time.sleep(0.5)

GPIO.cleanup()
