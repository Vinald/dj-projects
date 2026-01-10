from django.http import HttpResponseRedirect, HttpResponseBadRequest
from .models import Flight, Passenger
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def flight_list(request):
    return render(request, 'flights/flight_list.html', {
        'flights': Flight.objects.all()
    , 'title': 'Flight List'})


def flight_details(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    return render(request, 'flights/flight_details.html', {
        'flight': flight,
        'passengers': flight.passengers.all(),
        'non_passengers': Passenger.objects.exclude(flights=flight),
        'title': f'Flight {flight.flight_number} Details'
    })


def book(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)

    if request.method != "POST":
        return redirect('flight_details', flight.id)

    passenger_id = request.POST.get('passenger_id')
    if not passenger_id:
        return HttpResponseBadRequest("Missing passenger_id in form data")

    try:
        passenger = Passenger.objects.get(pk=int(passenger_id))
    except (Passenger.DoesNotExist, ValueError):
        return HttpResponseBadRequest("Invalid passenger selected")

    flight.passengers.add(passenger)
    return redirect('flight_details', flight.id)
