from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer
from .tasks import send_booking_confirmation_email

# Create your views here.

class ListingViewSet(ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        booking = serializer.save()
        email = booking.user.email
        send_booking_confirmation_email.delay(booking.email, booking)
        return booking