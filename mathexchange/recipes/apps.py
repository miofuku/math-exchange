import os
import csv
from django.db.models.signals import post_migrate
from django.core.files import File
from django.apps import AppConfig
from django.conf import settings
from mathexchange.accounts.apps import init_app


class EngineConfig(AppConfig):
    name = 'mathexchange.recipes'

    def ready(self):
        from . import signals
        # Triggered upon app initialization.
        post_migrate.connect(init_app, sender=self)
