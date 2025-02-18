"""
    Serializers for the listing and booking models
"""

from rest_framework import serializers
from .models import Listing, Booking


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = "__all__"
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
        # fields = ['user', 'listing', 'start_date', 'end_date', 'total_price', 'status']
            
