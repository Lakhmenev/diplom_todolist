from rest_framework import generics, permissions

from bot.models import TgUser
from bot.serializers import TgUserSerializer


class VerificationView(generics.GenericAPIView):
    model = TgUser
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TgUserSerializer

    def dispatch(self, request, *args, **kwargs):
        s: TgUserSerializer = self.get_serializer(data=request.data)
        s.is_valid(raise_exception=True)

        tg_user: TgUser = s.validated_data['tg_user']
        tg_user.user = self.request.user
        tg_user.save( )
