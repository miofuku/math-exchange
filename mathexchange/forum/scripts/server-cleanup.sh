#!/bin/bash

# Load the conda commands.
source ~/miniconda3/etc/profile.d/conda.sh

cd /export/www/mathexchange/

export POSTGRES_HOST=/var/run/postgresql

# Activate the conda environemnt.
conda activate engine

# Stop on errors.
set -ue

# Set the configuration module.
export DJANGO_SETTINGS_MODULE=conf.run.site_settings

python manage.py cleanup

python manage.py sitemap