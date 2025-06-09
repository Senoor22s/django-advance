from django.urls import path
from .. import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

urlpatterns = [
    path("registration/", views.RegistrationAPIView.as_view(), name="registration"),
    path("token/login/", views.CustomObtainAuthToken.as_view(), name="token-login"),
    path("token/logout/", views.CustomDiscardAuthToken.as_view(), name="token-logout"),
    path("jwt/create/", views.CustomTokenObtainPairView.as_view(), name="jwt-create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
    path("change-password", views.ChangePasswordAPIView.as_view(), name="change-password"),
    path("test-email", views.TestEmailSend.as_view(), name="test-email"),
    path(
        "activation/confirm/<str:token>", views.ActivationAPIView.as_view(), name="activation"
    ),
    path("activation/resend", views.ActivationResendAPIView.as_view(), name="activation"),
]
