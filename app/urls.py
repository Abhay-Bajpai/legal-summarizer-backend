from django.urls import path
from .views import UploadView, DocumentListView, DocumentDetailView

urlpatterns = [
    path('upload/', UploadView.as_view(), name='upload'),
    path('documents/', DocumentListView.as_view(), name='documents'),
    path('documents/<uuid:pk>/', DocumentDetailView.as_view(), name='document-detail'),
]
