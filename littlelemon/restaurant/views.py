from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Booking, Menu
from . import serializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


class MenuView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = serializer.MenuSerializer


class SingleMenuView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = serializer.MenuSerializer


class BookingView(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = serializer.BookingSerializer
