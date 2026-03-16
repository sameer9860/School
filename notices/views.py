from rest_framework.generics import ListAPIView
from .models import Notice
from .serializers import NoticeSerializer


class NoticeListAPIView(ListAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
