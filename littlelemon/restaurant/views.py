from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Booking, Menu
from . import serializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from django.http import JsonResponse
from django.core import serializers as ser

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
    bookings = Booking.objects.all()
    booking_json = ser.serialize('json', bookings)
    return render(request, 'bookings.html', {"bookings": booking_json})


class MenuView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = serializers.MenuSerializer


class SingleMenuView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = serializers.MenuSerializer


class BookingView(ListCreateAPIView):
    @csrf_exempt
    def get(self, request):
        query = Booking.objects.all()
        serializer = serializers.BookingSerializer(query, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request):
        query = Booking()
        query.name = request.data['name']
        query.no_of_guests = request.data['no_of_guests']
        query.bookingdate = request.data['bookingdate']
        query.save()
        serializer = serializers.BookingSerializer(query)
        return Response(serializer.data)
