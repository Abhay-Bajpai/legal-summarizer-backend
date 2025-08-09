from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'original_filename', 'uploaded_at', 'file', 'text', 'summary', 'summary_type', 'length']
        read_only_fields = ['id', 'uploaded_at', 'text', 'summary']

class UploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    summary_type = serializers.CharField(required=False)
    length = serializers.CharField(required=False)
