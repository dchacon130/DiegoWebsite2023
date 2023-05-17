from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("developer", views.developer, name="developer"),
    path("tester", views.tester, name="tester"),

    path("expQA", views.expQA, name="expQA"),
    path("knowledgeQa", views.knowledgeQa, name="knowledgeQa"),

    path("aboutDev", views.aboutDev, name="aboutDev"),
    path("projectsDev", views.projectsDev, name="projectsDev"),
]