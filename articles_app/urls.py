from django.urls import path, include
from rest_framework import routers
from .views import ArticlesViewSet

router = routers.SimpleRouter()

router.register(r'articles', ArticlesViewSet)

urlpatterns = router.urls
app_name = "articles"
urlpatterns = [path('', include(router.urls))]

# urlpatterns += router.urls
