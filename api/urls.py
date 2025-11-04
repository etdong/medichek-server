from django.urls import path
from . import views

urlpatterns = [
    path("health/", views.health, name="health"),
    path("sessions/", views.list_sessions, name="list_sessions"),
    path("sessions/create/", views.create_session, name="create_session"),
    path("sessions/<str:session_id>/", views.get_session, name="get_session"),
    path("sessions/<str:session_id>/update/", views.update_session, name="update_session"),
]
