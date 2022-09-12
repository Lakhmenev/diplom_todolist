from core.serializers import CreateUserSerializer
from rest_framework import generics


class SignupView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer


# class LoginView(generics.GenericAPIView):
#     serializer_class = LoginSerializer

    # def post
