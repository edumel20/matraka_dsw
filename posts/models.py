from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)
    content = models.TextField()
    writer = models.ForeignKey('members.Member', related_name='posts')
    editor = models.ForeignKey('members.Member', related_name='posts')

    def __str__(self):
        return f'PK={self.pk}: {self.title}'
