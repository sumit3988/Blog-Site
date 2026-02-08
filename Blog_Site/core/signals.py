from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from post.models import Post

@receiver(post_save,sender=Post)
def handle_post_publish(sender,instance,created,**kwargs):
    if instance.status==Post.Status.PUBLISHED and instance.published_at is None:
        instance.published_at=timezone.now()
        instance.save(update_fields=["published_at"])
        