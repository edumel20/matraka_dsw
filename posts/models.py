from django.db import models
from django.urls import reverse
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
    rating = models.FloatField(default=0)
    labels = models.ManyToManyField(
        'labels.Label',
        related_name='posts',
        blank=True,
    )

    def __str__(self):
        return f'PK={self.pk}: {self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

        def get_absolute_url(self):
            return reverse('posts:post-detail', args=[self.slug])


class PostLabelingDetail(models.Model):
    post = models.ForeignKey(
        'posts.Post',
        related_name='post_labeling_details',
        on_delete=models.CASCADE,
    )
    label = models.ForeignKey(
        'labels.Label',
        related_name='post_labeling_details',
        on_delete=models.CASCADE,
    )
    reason = models.CharField(max_length=256)
    labelled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'label')

    def __str__(self):
        return f'{self.reason} ({self.labelled_at.strftime("%d-%m-%Y")})'
