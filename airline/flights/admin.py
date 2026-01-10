from django.contrib import admin
from .models import Flight, Airport, Passenger


class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'departure', 'arrival', 'duration')


class AirportAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'city', 'country')


class PassengerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    filter_horizontal = ('flights',)

admin.site.register(Flight, FlightAdmin)
admin.site.register(Airport, AirportAdmin)
admin.site.register(Passenger, PassengerAdmin)