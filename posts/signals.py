from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Post
from .tasks import send_message


@receiver(post_save, sender=Post)
def notify_administrator_with_new_post(sender, instance, created, **kwargs):
    if created:
        msg = f'Post #{instance.pk} has been created!'
        send_message('admin', msg)
