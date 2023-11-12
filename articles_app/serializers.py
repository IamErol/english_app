from rest_framework.serializers import ModelSerializer
from .models import Articles, FavouritedArticle
from .models import Pictures
from rest_framework import serializers


class ArticlesSerializer(ModelSerializer):
    """
    Serializer for articles model.
    """

    class Meta:
        model = Articles
        fields = '__all__'


class ImageSerializer(ModelSerializer):
    """
    Serializer for pictures model.
    """

    class Meta:
        model = Pictures
        fields = ['id', 'image']
        extra_kwargs = {'id': {'read_only': True}, 'image': {'write_only': True}}


class FavouritedArticleSerializer(ModelSerializer):
    """
    Serializer for featured articles model.
    """

    class Meta:
        model = FavouritedArticle
        fields = '__all__'


class ReturnImagesSerializer(ModelSerializer):
    """
    Serializer for resized images return.
    """

    el = serializers.ImageField(source='image_1600_1200')
    lg = serializers.ImageField(source='image_1366_768')
    md = serializers.ImageField(source='image_1024_768')
    sm = serializers.ImageField(source='image_800_480')
    es = serializers.ImageField(source='image_480_320')

    class Meta:
        model = Pictures
        fields = ('el', 'lg', 'md', 'sm', 'es')
