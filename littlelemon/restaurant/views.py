from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Booking, Menu
from . import serializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from datetime import datetime

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def menuitems(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, 'menu_item.html', {"menu_item": menu_item})


def book(request):
    return render(request, 'book.html', {})


def reservations(request):
    return render(request, 'bookings.html', {})


class MenuView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = serializer.MenuSerializer


class SingleMenuView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = serializer.MenuSerializer


class BookingView(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = serializer.BookingSerializer


@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.load(request)
        exist = Booking.objects.filter(reservation_date=data['reservation_date']).filter(
            reservation_slot=data['reservation_slot']).exists()
        if exist == False:
            booking = Booking(
                first_name=data['first_name'],
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot'],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json')

    date = request.GET.get('date', datetime.today().date())

    bookings = Booking.objects.all().filter(reservation_date=date)
    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json')
