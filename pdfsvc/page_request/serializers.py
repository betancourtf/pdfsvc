from rest_framework import serializers

from page_request.models import PageRequest


class PageRequestSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PageRequest
        fields = ("url", "status", "error_msg", "pdf_file", "owner")
        read_only_fields = ("status", "error_msg", "pdf_file", "owner")
