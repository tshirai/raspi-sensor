#! /bin/bash
LANG=C
echo START
date
cd $(dirname $0)
pwd
pipenv run main-prod
echo END
echo
