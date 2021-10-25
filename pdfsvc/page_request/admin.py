from django.contrib import admin

from .models import PageRequest


@admin.register(PageRequest)
class PageRequestAdmin(admin.ModelAdmin):
    fields = ("url", "status", "error_msg", "pdf_file")
    readonly_fields = ("status", "error_msg", "pdf_file")
