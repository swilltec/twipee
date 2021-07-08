from django.apps import AppConfig
from django.db.utils import OperationalError


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    
    def ready(self):
        from .utils import scheduler
        try:
            scheduler.start_job()
        except OperationalError as ex:
            print(ex)
