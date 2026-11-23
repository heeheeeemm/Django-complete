
from django.urls import path, include

# 현재 디렉토리로부터 views.py
from . import views

app_name = "accounts"

urlpatterns = [
    path('login/', views.login, name = "login"),
    path('logout/', views.logout, name = "logout"),
    path('signup/', views.signup, name = "signup"),
]