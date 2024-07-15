from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'


class CustomAppNameConfig(AppConfig):
    name = 'user'
    verbose_name = 'Guezza Modules'

