from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from page_request.serializers import PageRequestSerializer
from page_request.models import PageRequest


class PageRequestViewSet(viewsets.ModelViewSet):
    queryset = PageRequest.objects.none()
    serializer_class = PageRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise
        return PageRequest.objects.filter(owner=self.request.user)
