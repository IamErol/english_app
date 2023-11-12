from django.urls import path, include
from rest_framework import routers
from .views import ArticlesViewSet, ImageView

router = routers.SimpleRouter()

router.register(r'articles', ArticlesViewSet, basename='articles')
router.register(r'image', ImageView, basename='upload_image')

# urlpatterns = router.urls
app_name = "articles"
urlpatterns = [path('', include(router.urls))]
