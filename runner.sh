#!/bin/sh
uwsgi --http-socket :5000 --plugin python --wsgi-file app.wsgi 
# Startup the cmd
