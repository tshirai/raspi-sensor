#! /usr/bin/env python


import argparse
from helper import google_spreadsheet as sheet
from helper import raspi, dht, co2
from helper import util

SHEET_NAME = 'HomeData'
TEST_SHEET_NAME = 'HomeDataTest'


def is_valid_value(value):
    return type(value) is float or type(value) is int


def status(key, value):
    if not is_valid_value(value):
        return False

    if key == 'raspi_temperature':
        if value > 60:
            return 'normal'
        else:
            return 'high'
    elif key == 'room_temperature':
        if value < 22:
            return 'low'
        elif value > 27:
            return 'high'
        else:
            return 'normal'
    elif key == 'room_humidity':
        if value < 40:
            return 'low'
        else:
            return 'normal'
    else:
        print(f"WARN: {key} is not supported.")
        return 'normal'


def to_line(header, data):
    lined = []
    for key in header:
        value = data.get(key, '')
        lined.append(value)
    return lined


def update(sheet_name):
    print("Fetching temperature and humidity...")
    dht_result = dht.read()
    print("Fetching CO2 level...")
    co2_result = co2.formatted()
    data = {
        'timestamp': util.now().strftime('%Y-%m-%d %H:%M:%S'),
        'raspi_temperature': raspi.formatted_temperature(),
        'room_temperature': dht_result[0],
        'room_humidity': dht_result[1],
        'room_co2': co2_result[0],
    }

    header = sheet.header(sheet_name)
    print(header)
    lined = to_line(header, data)
    sheet.append(sheet_name, lined)


def parse_args():
    options = {}
    parser = argparse.ArgumentParser()
    parser.add_argument('--prod', dest='prod', action='store_true')
    args = parser.parse_args()
    if args.prod:
        options['sheet_name'] = SHEET_NAME
    else:
        options['sheet_name'] = TEST_SHEET_NAME
    return options


def main():
    options = parse_args()
    update(options['sheet_name'])


if __name__ == '__main__':
    main()
