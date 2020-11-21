#! /usr/bin/env python

def get_temperature():
    try:
        with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
            return int(f.read()) / 1000.0
    except ValueError:
        return None


def formatted_temperature():
    value = get_temperature()
    if value is None:
        return ''
    else:
        return round(value, 1)
