#! /usr/bin/env python

import co2meter as co2
from functools import lru_cache


@lru_cache(maxsize=1)
def get_instance():
    return co2.CO2monitor()


def read():
    try:
        mon = get_instance()
        data = mon.read_data()
        # return (co2 level, temperature)
        return (data[1], data[2])
    except OSError:
        return None


def formatted():
    value = read()
    if value is None:
        print("WARN: Unknown error about USB CO2 monitor.")
        return ('', '')
    else:
        return value


def main():
    try:
        mon = get_instance()
        print(mon.info)
    except OSError as e:
        print(e)
        print("ERROR: Unknown error about USB CO2 monitor.")
        return

    result = read()
    print("CO2 level: %d" % result[0])
    print("Temperature: %-3.1f" % result[1])


if __name__ == '__main__':
    main()
