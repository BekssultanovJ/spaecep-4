from django.urls import path

from account.views import *
from product.contrib.auth.view import LogoutLogin
from django.urls import path

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('register/success/', SuccessfulRegistrationView.as_view(), name='register-success'),
    path('activate/<str:code>/', ActivationView.as_view(), name='activate'),
    path('login/', SigninView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='Logout'),
    path('change_password/', ChangePasswordView.as_view(), name='change-password'),
    path('forgot_password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('forgot_password/complete.', ForgotPasswordCompleteView.as_view(), name='forgot-password-complete'),
]