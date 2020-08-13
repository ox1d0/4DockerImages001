#!/bin/sh
source ../NginexAuto001 && nohup flask run & 
# Startup the cmd
exec "$@"
