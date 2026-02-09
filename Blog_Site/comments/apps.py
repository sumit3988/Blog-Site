from django.apps import AppConfig


class CommentsConfig(AppConfig):
    name = 'comments'
class PostsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "posts"

    def ready(self):
        import posts.signals
