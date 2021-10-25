from django.apps import AppConfig


class PageRequestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'page_request'

    def ready(self):
        import page_request.signals