from rest_framework import generics

from core.serializers import CreateUserSerializer


class SignupView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer


# class LoginView(generics.GenericAPIView):
#     serializer_class = LoginSerializer

    # def post

