import RPi.GPIO as GPIO

fan1 = 12
fan2 = 13

led = [7, 29, 8, 10]

def initFan(fan_1, fan_2):
    GPIO.setwarnings(False)
    GPIO.setup(fan_1, GPIO.OUT, initial=False)
    GPIO.setup(fan_2, GPIO.OUT, initial=False)

def onFan():
    GPIO.output(fan1, GPIO.HIGH)
    GPIO.output(fan2, GPIO.LOW)

def offFan():
    GPIO.output(fan1, GPIO.LOW)
    GPIO.output(fan2, GPIO.LOW)

def initLed():
    for i in led:
        GPIO.setup(i, GPIO.OUT)

def onLed():
    for j in led:
        GPIO.output(j, GPIO.HIGH)

def offLed():
    for k in led:
        GPIO.output(k, GPIO.LOW)

def exit():
    GPIO.cleanup()

def main():
    GPIO.setmode(GPIO.BOARD)
    initFan(fan1, fan2)
    initLed()
    print("---------------")
    print("1. fan on")
    print("2. fan off")
    print("3. led on")
    print("4. led off")
    print("5. exit")
    print("---------------")
    while(True):
        a = int(input("select number: "))
        if a == 1:
            onFan()
        elif a == 2 :
            offFan()
        elif a == 3 :
            onLed()
        elif a == 4 :
            offLed()
        elif a == 5 :
            exit()
            break


if __name__ == "__main__":
    main()
