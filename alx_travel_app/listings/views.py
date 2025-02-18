from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer
from .tasks import send_booking_confirmation_email
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class ListingViewSet(ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        serializer.save() 
        send_booking_confirmation_email.delay(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
