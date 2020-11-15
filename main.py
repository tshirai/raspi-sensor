#! /usr/bin/env python


import argparse
import sys
from helper import google_spreadsheet as sheet
from helper import dht
from helper import raspi
from helper import util

SHEET_NAME = 'HomeData'
TEST_SHEET_NAME = 'HomeDataTest'


def to_line(header, data):
    lined = []
    for key in header:
        value = data.get(key, '')
        lined.append(value)
    return lined


def update(sheet_name):
    result = dht.read()
    data = {
        'timestamp': util.now().strftime('%Y-%m-%d %H:%M:%S'),
        'raspi_temperature': raspi.formatted_temperature(),
        'room_temperature': result[0],
        'room_humidity': result[1],
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
