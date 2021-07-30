import RPi.GPIO as GPIO
from time import sleep

on = 1
off = 0
fan_pin1 = 18
fan_pin2 = 27

def initFan(fanpin1, fanpin2):
    GPIO.setwarnings(False)
    GPIO.setup(fanpin1, GPIO.OUT, initial=False)
    GPIO.setup(fanpin2, GPIO.OUT, initial=False)

def onFan():
    GPIO.output(fan_pin1, GPIO.HIGH)
    GPIO.output(fan_pin2, GPIO.LOW)

def offFan():
    GPIO.output(fan_pin1, GPIO.LOW)
    GPIO.output(fan_pin2, GPIO.LOW)

def controlFan(motion):
    if(motion == on):
        onFan()
    else:
        offFan()

def main():
    GPIO.setmode(GPIO.BCM)
    initFan(fan_pin1, fan_pin2)
    print("setup fan pin as outputs")
    print("main() program")

    try:
        while True:
            controlFan(on)
            sleep(5.0)
            controlFan(off)
            sleep(3.0)
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
