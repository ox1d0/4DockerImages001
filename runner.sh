#!/bin/sh
#uwsgi --http-socket :5000 --plugin python --wsgi-file app.wsgi &
#printf "uwsgi Done\n"
# Startup the cmd
#nginx
#printf "Running flask demo only\n"
nohup flask run &

