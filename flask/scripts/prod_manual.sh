#!/usr/bin/env bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
pip install uwsgi
export RDS_USERNAME=root
export RDS_PASSWORD=my-secret-pw
export RDS_HOSTNAME=172.17.0.2
export RDS_DB_NAME=notejam
python db_prod.py
uwsgi --http 127.0.0.1:5000 --wsgi-file notejam/wsgi.py --enable-threads --master