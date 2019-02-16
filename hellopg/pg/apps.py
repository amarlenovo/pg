from django.apps import AppConfig

class PgConfig(AppConfig):
    name = 'pg'
    def ready(self):
        import pg.signals
