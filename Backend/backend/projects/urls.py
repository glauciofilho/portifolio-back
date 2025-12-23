from django.urls import path
from .views import project_detail

urlpatterns = [
    path('projects/<int:project_id>/', project_detail),
]