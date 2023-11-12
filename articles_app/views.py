from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from .serializers import ArticlesSerializer, ImageSerializer, ReturnImagesSerializer
from .models import Articles, Pictures


class ArticlesViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the articles.
    """
    serializer_class = ArticlesSerializer
    permission_classes = [IsAdminUser]
    queryset = Articles.objects.all()


class ImageView(viewsets.ModelViewSet):
    """
    Image crud viewset.
    """

    permission_classes = [AllowAny]
    queryset = Pictures.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReturnImagesSerializer
        return ImageSerializer
