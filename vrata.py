import RPi.GPIO as GPIO
import time

channel = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

def motor_on(pin):
    GPIO.output(pin, GPIO.HIGH)

def motor_off(pin):
    GPIO.output(pin, GPIO.LOW)

if __name__ == '__main__':
    try:
        motor_on(channel)
        time.sleep(3)
        print("Vrata otvorena...")
        motor_off(channel)
        time.sleep(3)
        motor_on(channel)
        time.sleep(3)
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()
        
