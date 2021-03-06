#! /usr/bin/env python

from __future__ import print_function
import json
import pickle
import os.path
import string
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from . import util


# Set SHEET_ID
with open(util.project_path('secrets', 'sheet.json'), 'r') as f:
    config = json.loads(f.read())
    SHEET_ID = config['sheet_id']


####################################
# Google Spreadsheet
####################################
def get_sheet_url():
    return f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/edit"


def get_sheets():
    TOKEN = util.project_path('secrets', 'token.pickle')
    CREDENTIALS = util.project_path('secrets', 'google-api-credentials.json')
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(TOKEN):
        with open(TOKEN, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(TOKEN, 'wb') as token:
            pickle.dump(creds, token)
    service = build('sheets', 'v4', credentials=creds)
    return service.spreadsheets()


def append(sheet_name, data):
    # ex. APITest!A:E
    sheet_range = f"{sheet_name}!A:{string.ascii_uppercase[len(data)]}"
    body = {
        'values': [data],
    }
    sheets = get_sheets()
    print("Request:")
    print(f"  sheet_range: {sheet_range}")
    print(f"  body: {body}")
    result = sheets.values().append(spreadsheetId=SHEET_ID,
                                    range=sheet_range,
                                    valueInputOption='USER_ENTERED',
                                    body=body).execute()

    print("Response:")
    print(f"  updated: {result['updates']['updatedRange']}")


def header(sheet_name, last_column='Z'):
    sheet_range = f"{sheet_name}!A:{last_column}"
    sheets = get_sheets()
    result = sheets.values().get(spreadsheetId=SHEET_ID,
                                 range=sheet_range).execute()
    return result.get('values')[0]


def main():
    print(get_sheet_url())
    append('APITest', [0, 1, 2, 3, 4])


if __name__ == '__main__':
    main()
