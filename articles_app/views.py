from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from PIL import Image
from .serializers import ArticlesSerializer
from .models import Articles
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your views here.
class ArticlesViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the articles.
    """
    serializer_class = ArticlesSerializer
    # permission_classes = [IsAdminUser]
    queryset = Articles.objects.all()

    def perform_create(self, serializer):
        image = serializer.validated_data['picture']
        img = Image.open(image)

        # Resize the image (e.g., to 300x300 pixels)
        img.resize((800, 480))

        # Save the resized image back to the serializer
        # serializer.validated_data['picture_1600_1200'] = img
        output = BytesIO()
        img.save(output, format='JPEG')  # Save as JPEG or any desired format
        output.seek(0)

        # Create a new file with a unique name for the resized image
        resized_image = InMemoryUploadedFile(
            output,
            'ImageField',
            f"resized_",  # Unique name for the resized image
            'image/jpeg',
            output.tell(),
            None
        )

        # Save the resized image as a new file
        serializer.validated_data['picture_1600_1200'] = resized_image
        # serializer.save()
        serializer.save()
