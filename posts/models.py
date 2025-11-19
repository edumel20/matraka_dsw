from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    class Category(models.TextChoices):
        SOCIETY = 'SOC', 'Society'
        EDUCATION = 'EDU', 'Education'
        HEALTH = 'HLT', 'Health'
        CULTURE = 'CUL', 'Culture'
        TECH = 'TEC', 'Technology'

    class Rating(models.IntegerChoices):
        VERY_BAD = 1
        BAD = 2
        AVERAGE = 3
        GOOD = 4
        EXCELLENT = 5

    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)
    content = models.TextField()
    category = models.CharField(max_length=3, choices=Category, default=Category.SOCIETY)
    rating = models.IntegerField(choices=Rating, default=Rating.AVERAGE)

    def __str__(self):
        return f'PK={self.pk}: {self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
