try:
    from .celery import app as celery_app
    __all__ = ['celery_app']
except ImportError as exc:
    pass

VERSION = '0.0.1'
