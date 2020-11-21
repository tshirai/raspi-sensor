#! /bin/bash

LANG=C
echo START
date
export PYENV_ROOT=~/.pyenv
PATH=~/.pyenv/bin:$PATH
echo $PATH
eval "$(pyenv init -)"

cd $(dirname $0)
pwd
pipenv run main-prod
echo END
echo
