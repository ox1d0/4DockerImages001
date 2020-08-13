#!/bin/sh
source NginexAuto001/bin/activate && nohup flask run & 
# Startup the cmd
exec "$@"
