from django.db import models
import uuid

class Document(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    original_filename = models.CharField(max_length=512)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='uploads/')
    text = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    summary_type = models.CharField(max_length=32, default='extractive')
    length = models.CharField(max_length=16, default='short')

    def __str__(self):
        return f"{self.original_filename} ({self.id})"
