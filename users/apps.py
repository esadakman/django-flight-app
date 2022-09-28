from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"
# signalsin çalışması için def ready'i yazmamız gerekiyor
    def ready(self):
        import users.signals