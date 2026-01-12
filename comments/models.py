from django.db import models


class Comment(models.Model):
    alias = models.CharField(max_length=128)
    content = models.TextField()
    post = models.ForeignKey('posts.Post', related_name='comments', on_delete=models.CASCADE)
