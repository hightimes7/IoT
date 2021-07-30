import RPi.GPIO as GPIO

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world"

@app.route('/led/<onoff>')
def ledonoff(onoff):
    if onoff == "on":
        print("Led Turn on")
        GPIO.output(4,1)
        return "LED on"
    elif onoff == "off":
        print("Led Turn off")
        GPIO.output(4,0)
        return "LED off"

if __name__ == "__main__":
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)
    app.run(host='0.0.0.0', port=5000, debug=True)
    GPIO.cleanup()
