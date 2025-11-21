from django.db import models


class Reason(models.Model):
    post = models.ForeignKey(
        'posts.Post',
        related_name='seals',
        on_delete=models.CASCADE,
    )
    label = models.ForeignKey(
        'labels.Label',
        related_name='seals',
        on_delete=models.CASCADE,
    )
    labelled_because = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.post} ⇔ {self.label} ({self.labelled_because})'
