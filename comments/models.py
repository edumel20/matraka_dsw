from django.conf import settings
from django.db import models


class Comment(models.Model):
    alias = models.CharField(max_length=128)
    content = models.TextField(max_length=256)
    post = models.ForeignKey(
        'posts.Post',
        related_name='comments',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    created = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)


    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return f'{self.alias or "Anonymous"} on {self.post}'