from django.apps import AppConfig


class UseranalyticsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'useranalytics'

    def ready(self):
        import useranalytics.signals
