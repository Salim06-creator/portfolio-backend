from django.urls import path
from .views import (
    profile,
    projects,
    qualifications
)

urlpatterns = [
    path('profile/', profile),
    path('projects/', projects),
    path('qualifications/', qualifications),
]