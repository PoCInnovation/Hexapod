import RPI.GPIO as GPIO
import time

class distanceSensor:
    def __init__(self, TRIGGER, ECHO):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        self.GPIO_TRIGGER = TRIGGER
        self.GPIO_ECHO = ECHO

        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)

    def getDistance(self):
        GPIO.output(self.GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)

        startTime = time.time()
        stopTime = time.time()

        while GPIO.input(self.GPIO_ECHO) == 0:
            startTime = time.time()
            if stopTime - startTime > 1:
                break

        timeElasped = stopTime - startTime
        distance = (timeElasped * 34300) / 2

        if distance < 0 or distance > 1000:
            return 0
        return distance