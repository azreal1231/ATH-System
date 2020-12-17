apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
apt install python3-venv
python3.8 -m venv venv
source venv/bin/activate
pip3 install wheel
pip3 install gunicorn flask
pip3 install couchdb