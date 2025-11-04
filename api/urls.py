from django.urls import path
from . import views

urlpatterns = [
    path("health/", views.health, name="health"),
    path("analysis/submit/", views.receive_data, name="receive_data"),
]
