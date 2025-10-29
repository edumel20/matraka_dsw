from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)
    content = models.TextField()

    def __str__(self):
        return f'PK={self.pk}: {self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
