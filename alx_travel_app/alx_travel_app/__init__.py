from __future__ import absolute_import, unicode_literals

# Importer Celery dès le démarrage de Django
from .celery import app as celery_app

__all__ = ('celery_app',)
