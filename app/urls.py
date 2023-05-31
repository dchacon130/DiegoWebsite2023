from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tester", views.tester, name="tester"),
    path("developer", views.developer, name="developer"),
    path("knowledge", views.knowledge, name="knowledge"),
    path("experience", views.experience, name="experience"),
    path("knowledgeDev", views.knowledgeDev, name="knowledgeDev"),
    path("experienceDev", views.experienceDev, name="experienceDev"),
]