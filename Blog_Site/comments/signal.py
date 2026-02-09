from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Comment


@receiver(pre_save, sender=Comment)
def auto_approve_staff_comments(sender, instance, **kwargs):
    if instance.user.is_staff:
        instance.is_approved = True
