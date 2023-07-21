from django.apps import AppConfig


class BlogConfig(AppConfig):
    """ App configuration"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
