from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_booking_confirmation_email(email, booking_details):
    subject = 'Your Booking Confirmation 🚀'

    message = f"""
    Hello {booking_details.get('user').last_name} {booking_details.get('user').first_name}, ,

    We're excited to confirm your booking! 🎉

    📋 **Booking Details:**  
    Listing: {booking_details.get('listing')}  
    ✅ Status: Confirmed  
    📅 Dates: From {booking_details.get('start_date')} to {booking_details.get('end_date')}  
    💰 Total Price: {booking_details.get('total_price')} €

    If you have any questions, feel free to reach out to us.

    Thank you for choosing ALX Travel App! 🌍
    """

    send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
    return 'Confirmation email sent successfully ✅'
