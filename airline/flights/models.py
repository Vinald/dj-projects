from django.db import models


class Airport(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.code} - {self.name} ({self.city}, {self.country})"

class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    departure = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    arrival = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.flight_number}: {self.departure} to {self.arrival}"


class Passenger(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    flights = models.ManyToManyField(Flight, blank=True, related_name='passengers')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"