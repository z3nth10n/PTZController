#!/bin/bash
apt-get install libxml2-dev libxslt-dev python3-lxml
pip install -r requirements.txt
curl https://pyenv.run | bash
pyenv install 3.9.20
python3.9 -m venv ./venv
source venv/bin/activate
pip install --upgrade pip setuptools
pip install -r requirements.txt
screen -S ptz
python start.py