from rest_framework.serializers import ModelSerializer
from .models import Articles, Pictures, FavouritedArticle
from .models import Pictures


class ArticlesSerializer(ModelSerializer):
    """Serializer for articles model."""

    class Meta:
        model = Articles
        fields = '__all__'


class ImageSerializer(ModelSerializer):
    """Serializer for pictures model."""

    class Meta:
        model = Pictures
        fields = ['image']


class FavouritedArticleSerializer(ModelSerializer):
    """Serializer for featured articles model."""

    class Meta:
        model = FavouritedArticle
        fields = '__all__'




