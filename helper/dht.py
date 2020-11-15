#! /usr/bin/env python

import RPi.GPIO as GPIO
import dht11
from functools import lru_cache


@lru_cache(maxsize=128)
def get_instance():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()

    # read data using pin 4
    return dht11.DHT11(pin=4)


def read():
    result = get_instance().read()
    if result.is_valid():
        return (result.temperature, result.humidity)
    else:
        return ('', '')


def main():
    result = read()
    print("Temperature: %-3.1f C" % result[0])
    print("Humidity: %-3.1f %%" % result[1])


if __name__ == '__main__':
    main()
