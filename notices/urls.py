from django.urls import path
from .views import NoticeListAPIView

urlpatterns = [
    path("", NoticeListAPIView.as_view()),
]
