# Generated by Django 4.2.6 on 2023-10-26 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles_app', '0002_articles_picture_url_articles_publish_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='slug',
        ),
    ]
