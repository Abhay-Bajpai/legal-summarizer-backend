from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DocumentSerializer, UploadSerializer
from .models import Document
from .utils.pdf_utils import extract_text_from_pdf
from .utils.summarizer import summarize_text
import os

class UploadView(APIView):
    def post(self, request, format=None):
        serializer = UploadSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        file = serializer.validated_data['file']
        summary_type = serializer.validated_data.get('summary_type', 'extractive')
        length = serializer.validated_data.get('length', 'short')

        # save model (Django will store file)
        doc = Document.objects.create(original_filename=file.name, file=file, summary_type=summary_type, length=length)
        tmp_path = doc.file.path
        text = ''
        try:
            if tmp_path.lower().endswith('.pdf') or True:
                text = extract_text_from_pdf(tmp_path)
        except Exception:
            try:
                with open(tmp_path, 'r', errors='ignore') as f:
                    text = f.read()
            except Exception:
                text = ''

        doc.text = text
        doc.summary = summarize_text(text or '', length=length)
        doc.save()

        data = DocumentSerializer(doc).data
        return Response(data, status=status.HTTP_201_CREATED)

class DocumentListView(APIView):
    def get(self, request):
        docs = Document.objects.all().order_by('-uploaded_at')[:50]
        serializer = DocumentSerializer(docs, many=True)
        return Response(serializer.data)

class DocumentDetailView(APIView):
    def get(self, request, pk):
        try:
            doc = Document.objects.get(pk=pk)
        except Document.DoesNotExist:
            return Response(status=404)
        serializer = DocumentSerializer(doc)
        return Response(serializer.data)
