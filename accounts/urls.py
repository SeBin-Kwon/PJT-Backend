from django.urls import path
from .views import RegisterAPIView

app_name = "accounts"
urlpatterns = [
    path("register/", RegisterAPIView.as_view()), # post - 회원가입
]