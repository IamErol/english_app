from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Articles, Pictures, FavouritedArticle

from django.db import models
from django.urls import path

from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO

from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Pictures


class ArticlesSerializer(ModelSerializer):
    """Serializer for articles model."""

    class Meta:
        model = Articles
        fields = '__all__'


class ImageSerializer(ModelSerializer):
    """Serializer for pictures model."""
    # el = serializers.URLField()
    # lg = serializers.URLField()
    # md = serializers.URLField()
    # sm = serializers.URLField()
    # es = serializers.URLField()

    class Meta:
        model = Pictures
        fields = ['image']


class FavouritedArticleSerializer(ModelSerializer):
    """Serializer for featured articles model."""

    class Meta:
        model = FavouritedArticle
        fields = '__all__'




