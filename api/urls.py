from django.urls import path
from .views import UploadView

urlpatterns = [
    path('api/extract_resume', UploadView )
]
