from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.student_list, name="student-list"),
    # TODO 4 (E2.d): ruta pentru detaliile unui student
    path("students/<int:student_id>/", views.student_detail, name="student-detail"),
    # TODO 5 (E2.d): ruta pentru verificarea starii serviciului
    path("health/", views.health, name="health"),
]
