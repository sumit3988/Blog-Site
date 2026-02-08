from django.db import models
from django.conf import settings
from posts.models import Post


# Create your models here.

class Comment(models.Model):
    post=models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"


    )

    user=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    content=models.TextField()

    is_approved=models.BooleanField(default=False)

    created_at =models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions=[
            ("moderate_comment","Can approve or reject comments"),

        ]
    def __str__(self):
        return f"Comment by {self.user}"