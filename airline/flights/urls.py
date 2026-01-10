from django.urls import path
from . import views


urlpatterns = [
    path('', views.flight_list, name='flight_list'),
    path('<int:flight_id>/', views.flight_details, name='flight_details'),
    path('<int:flight_id>/book/', views.book, name='book'),
]
