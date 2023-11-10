from django.urls import path
from .views import (RegisterView,
                    VerifyEmail,
                    LogoutAPIView)

# app_name = 'user'

urlpatterns = [
    path('create/', RegisterView.as_view(), name='create'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('email-verify/', VerifyEmail.as_view(), name='email-verify'),
]