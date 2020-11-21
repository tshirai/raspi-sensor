#! /usr/bin/env python

import co2meter as co2
from functools import lru_cache


@lru_cache(maxsize=1)
def get_instance():
    return co2.CO2monitor()


def read():
    mon = get_instance()
    data = mon.read_data()
    # return (co2 level, temperature)
    return (data[1], data[2])


def main():
    mon = get_instance()
    print(mon.info)
    result = read()
    print("CO2 level: %d" % result[0])
    print("Temperature: %-3.1f" % result[1])


if __name__ == '__main__':
    main()
