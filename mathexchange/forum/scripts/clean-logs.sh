#!/bin/bash

# Stop on errors.
set -ue

# logs directory in export dir
DIR=/export/www/mathexchange/export/logs

# Truncate all logs
truncate -s 0 $DIR/*.log
