from rest_framework.serializers import ModelSerializer
from .models import Articles


class ArticlesSerializer(ModelSerializer):
    """Serializer for articles model."""

    class Meta:
        model = Articles
        fields = '__all__'
