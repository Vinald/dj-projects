from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Meetup

# Create your views here.
class MeetupListView(ListView):
    model = Meetup
    template_name = 'meetups/meetup_list.html'
    context_object_name = 'meetups'