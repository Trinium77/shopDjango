from django.urls import path
from .views import register, login_view, CustomPasswordChangeView, logout_user, forgot_password_view

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('logout/', logout_user, name='logout'),  # Utilisation correcte de logout_user
    path('forgot-password/', forgot_password_view, name='forgotPassword'),
]
