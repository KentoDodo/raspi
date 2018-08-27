import time, datetime
import RPi.GPIO as GPIO
from util.dht11 import DHT11

from setting import GPIO_PIN_DHT11
from util.temp_handler import save_to_temp


def dht11_run():
    # initialize GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()

    instance = DHT11(pin=GPIO_PIN_DHT11)

    while True:
        result = instance.read()
        if result.is_valid():
            save_to_temp({
                "datetime": datetime.datetime.now().isoformat(),
                "temperature": result.temperature,
                "humidity": result.humidity
            })

        time.sleep(1)
