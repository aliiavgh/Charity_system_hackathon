from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from applications.account import serializers
from rest_framework import status

User = get_user_model()


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.RegisterSerializer


class ActivationAPIView(generics.ListAPIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save(update_fields=['is_active', 'activation_code'])
            return Response({'msg': 'ваш аккаунт успешно активирован'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'msg': 'некоректный код активации'})


class ChangePasswordAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.ChangePasswordSerializer
    permission_classes = [IsAuthenticated]


class ForgotPasswordAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.ForgotPasswordSerializer


class ForgotPasswordConfirmAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.ForgotPasswordConfirmSerializer


class ForgotPasswordCodewordAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.ForgotPasswordCodewordSerializer
