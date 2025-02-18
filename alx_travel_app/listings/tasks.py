from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from .models import Listing


@shared_task
def send_booking_confirmation_email(data):
    user = User.objects.get(id=data['user'])
    print(f"Sending booking confirmation email... on email : {user.email}")
    
    
    subject = 'Booking Confirmation 🚀'
    message = f"""
    Hello {user.last_name} {user.first_name}, ,

    We're excited to confirm your booking! 🎉

    📋 **Booking Details:**  
    Listing: {Listing.objects.get(id=data['listing']).name}  
    ✅ Status: Confirmed
    📅 Dates: From {data['start_date']} to {data['end_date']}  
    💰 Total Price: {data['total_price']} € 

    If you have any questions, feel free to reach out to us.

    Thank you for choosing ALX Travel App! 🌍
    """

    send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list=[user.email], fail_silently=True, html_message=message)
    return 'Confirmation email sent successfully ✅'
