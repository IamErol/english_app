from django.db import models
from django.contrib.auth import get_user_model
from .image_processing import ImageResizer
import os
User = get_user_model()


def image_path(instance, filename):
    # return '/'.join(['pictures', str(instance.id)])
    ext = os.path.splitext(filename)[1]
    filename = f'{filename}'

    return os.path.join('pictures', filename)

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
    picture = models.ImageField(upload_to=image_path, null=True, blank=True)
    picture_1600_1200 = models.ImageField(upload_to=image_path, null=True, blank=True)
    picture_1366_768 = models.ImageField(upload_to=image_path, null=True, blank=True)
    picture_1024_768 = models.ImageField(upload_to=image_path, null=True, blank=True)
    picture_800_480 = models.ImageField(upload_to=image_path, null=True, blank=True)
    picture_480_320 = models.ImageField(upload_to=image_path, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = ImageResizer(self.picture.path)
        self.picture_1600_1338 = image.resize(size_choice='1600x1338')
        # self.picture_1366_768 = image.resize(size_choice='1366x768')
        # self.picture_1024_768 = image.resize(size_choice='1024x768')
        # self.picture_800_480 = image.resize(size_choice='800x480')
        # self.picture_480_320 = image.resize(size_choice='480x320')
        # return super(Articles, self).save(*args, **kwargs)
        image.save(self.picture_1600_1338.path)


class FavoritedArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Articles, related_name="article", on_delete=models.CASCADE)
