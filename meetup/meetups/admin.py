from django.contrib import admin
from .models import Meetup


class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')
    search_fields = ('title', 'description', 'location')


# Register your models here.
admin.site.register(Meetup, MeetupAdmin)
