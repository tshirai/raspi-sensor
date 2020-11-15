#! /usr/bin/env python

import os.path
from datetime import datetime, timedelta, timezone


def project_path(*paths):
    root = os.path.dirname(os.path.dirname(__file__))
    if root == '':
        root = '.'
    if len(paths) == 0:
        return root
    else:
        return os.path.join(root, *paths)


def now():
    jst = timezone(timedelta(hours=+9), 'JST')
    return datetime.now(jst)


def main():
    print(project_path())
    sheet_json = project_path('secrets', 'sheet.json')
    print(sheet_json)
    print(f"{sheet_json} exists?: {os.path.exists(sheet_json)}")

    print(now())


if __name__ == '__main__':
    main()
