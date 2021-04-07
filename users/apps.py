from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = "users"

    def ready(self):  # This function is required in order for signals to work
        import users.signals
