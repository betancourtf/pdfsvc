from django.conf import settings
from django.db import models


class PageRequest(models.Model):
    class Status(models.TextChoices):
        PENDING = "P", "Pending"
        GENERATING = "G", "Generating"
        READY = "R", "Ready"
        ERROR = "E", "Error"

    url = models.CharField(max_length=128)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.PENDING
    )
    error_msg = models.CharField(max_length=128, blank=True, null=True)
    pdf_file = models.FileField(
        upload_to=f"${settings.MEDIA_ROOT}/pdfs/", null=True, blank=True
    )

    def __str__(self):
        return f"{self.pk} ({self.url})"
