from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from applications.account import views

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view()),
    path('activate/<uuid:activation_code>', views.ActivationAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change_password/', views.ChangePasswordAPIView.as_view()),
    path('forgot_password/', views.ForgotPasswordAPIView.as_view()),
    path('forgot_password_confirm/', views.ForgotPasswordConfirmAPIView.as_view()),
    path('forgot_password_codeword/', views.ForgotPasswordCodewordAPIView.as_view()),

]