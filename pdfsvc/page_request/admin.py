from django.contrib import admin

from .models import PageRequest


@admin.register(PageRequest)
class PageRequestAdmin(admin.ModelAdmin):
    fields = ("url", "status", "error_msg", "pdf_file")
    readonly_fields = ("status", "error_msg", "pdf_file")

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.save()
