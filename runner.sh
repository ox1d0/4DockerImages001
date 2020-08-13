#!/bin/sh
nohup flask run & 
# Startup the cmd
exec "$@"
