#! /usr/bin/env python
"""
See https://developers.google.com/sheets/api/quickstart/python
"""
from helper import get_spreadsheets, SHEET_ID


def sample():
    SAMPLE_RANGE_NAME = 'Class Data!A2:E'

    sheets = get_spreadsheets()
    # Call the Sheets API
    result = sheets.values().get(spreadsheetId=SHEET_ID,
                                 range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[4]))


def main():
    sample()


if __name__ == '__main__':
    main()
