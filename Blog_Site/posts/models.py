from django.db import models
from django.conf import settings


class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        REVIEW = "review", "In Review"
        PUBLISHED = "published", "Published"

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT
    )

    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="reviewed_posts"
    )

    published_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = [
            ("submit_post", "Can submit post for review"),
            ("review_post", "Can review posts"),
            ("publish_post", "Can publish posts"),
        ]

    def __str__(self):
        return self.title
