from django.urls import path

from . import views

urlpatterns = [
    path("", views.challenges, name="challenges"),
    path("<int:month>/", views.challenge_by_number, name="challenge_by_number"),
    path("<str:month>/", views.challenge, name="challenge"),
]
