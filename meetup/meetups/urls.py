from django.urls import path
from . import views

urlpatterns = [
    path('meetups/', views.MeetupListView.as_view(), name='meetup-list'),
]
