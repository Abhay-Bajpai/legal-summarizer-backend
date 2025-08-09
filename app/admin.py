from django.contrib import admin
from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('original_filename', 'uploaded_at', 'id')
    readonly_fields = ('uploaded_at',)
