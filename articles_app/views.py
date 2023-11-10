from rest_framework import viewsets, status
from PIL import Image
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from .serializers import ArticlesSerializer, ImageSerializer
from .models import Articles, Pictures
from . import image_processing
class ArticlesViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the articles.
    """

    serializer_class = ArticlesSerializer
    permission_classes = [IsAdminUser]
    queryset = Articles.objects.all()

class UploadImage(viewsets.ModelViewSet):

    serializer_class = ImageSerializer
    permission_classes = [AllowAny]
    queryset = Pictures.objects.all()





