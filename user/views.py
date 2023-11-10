from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import DjangoUnicodeDecodeError, smart_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import (RegisterSerializer,
                          EmailVerificationSerializer,
                          LogoutSerializer)
from rest_framework import generics, status, permissions
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
import os

User = get_user_model()

class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return User.objects.none()

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])

        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relative_link = reverse('email-verify')
        absurl = 'http://' + current_site + relative_link + "?token=" + str(token)

        email_body = f"Hi {user.username} use this link to verify your email: {absurl}. " \
                     f"Link will expire in 1 hour."
        data = {'email_body': email_body, 'to_email': user.email,
                'email_subject': 'Verify your email.'}

        Util.send_email(data)

        return Response(user_data, status.HTTP_201_CREATED)


class VerifyEmail(generics.GenericAPIView):

    serializer_class = EmailVerificationSerializer

    def get_queryset(self):
        return User.objects.none()


    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, os.environ.get('DJANGO_SECRET_KEY'), algorithms='HS256')
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()

            return Response({'email': 'Successfully activated.'}, status=status.HTTP_200_OK)

        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation link is expired.'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.DecodeError as identifier:
            return Response({'error': 'Invalid token'}, status.HTTP_400_BAD_REQUEST)



class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer

    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return User.objects.none()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)