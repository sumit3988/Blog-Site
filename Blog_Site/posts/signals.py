from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from .models import Post


@receiver(post_save, sender=Post)
def handle_post_publish(sender, instance, created, **kwargs):
    """
    Side effects when a post is published
    """

    if instance.status == Post.Status.PUBLISHED:
        # Set published_at only once
        if instance.published_at is None:
            instance.published_at = timezone.now()
            instance.save(update_fields=["published_at"])
