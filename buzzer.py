import RPi.GPIO as GPIO
from time import sleep

buzzer_pin = 7

scale = [261, 294, 329, 349, 392, 440, 493, 523]

melodyList = [4,4,5,5,4,4,2,4,4,2,2,1,4,4,5,5,4,4,2,4,2,1,2,0]
noteDurations = [0.5,0.5,0.5,0.5,0.5,0.5,1,0.5,0.5,0.5,0.5,1,
                 0.5,0.5,0.5,0.5,0.5,0.5,1,0.5,0.5,0.5,0.5,1]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buzzer_pin, GPIO.OUT)
pwm = GPIO.PWM(buzzer_pin, 100)

def playBuzzer(melodyList, noteDurations):
    pwm.start(100)
    pwm.ChangeDutyCycle(50)
    for i in range(len(melodyList)):
        pwm.ChangeFrequency(scale[melodyList[i]])
        sleep(noteDurations[i])
    pwm.stop()

def main():
    print("start buzzer program ...")
    playBuzzer(melodyList, noteDurations)
    pwm.stop()
    try :
        while True:
            pass
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
