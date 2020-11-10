#! /usr/bin/env python
from helper import append_to_spreadsheet


def main():
    append_to_spreadsheet('APITest', [0, 1, 2, 3, 4])
    pass


if __name__ == '__main__':
    main()
