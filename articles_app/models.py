from django.db import models
from django.contrib.auth import get_user_model
from .image_processing import image_resize
import os

User = get_user_model()


def image_path(instance, filename):
    filename = f'{filename}'
    return os.path.join(filename)


class Articles(models.Model):
    LEVELS_CHOICES = [
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced'),
    ]
    title = models.CharField(max_length=255)
    content = models.TextField(null=False, blank=False)
    english_level = models.IntegerField(null=False, blank=False, choices=LEVELS_CHOICES, default="Beginner")
    publish_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.title)


class Pictures(models.Model):
    image = models.ImageField(upload_to=image_path, null=True, blank=True)
    image_1600_1200 = models.ImageField(upload_to=image_path, null=True, blank=True)
    image_1366_768 = models.ImageField(upload_to=image_path, null=True, blank=True)
    image_1024_768 = models.ImageField(upload_to=image_path, null=True, blank=True)
    image_800_480 = models.ImageField(upload_to=image_path, null=True, blank=True)
    image_480_320 = models.ImageField(upload_to=image_path, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.image:
            image_resize(image=self.image, instance=self)

        super(Pictures, self).save(*args, **kwargs)


class FavouritedArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Articles, related_name="article", on_delete=models.CASCADE)

