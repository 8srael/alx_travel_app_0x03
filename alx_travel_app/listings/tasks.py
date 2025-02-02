from celery import shared_task
from django.core.mail import send_mail
from alx_travel_app.settings import EMAIL_HOST_USER


@shared_task
def send_booking_confirmation_email(email, booking_details):
    subject = 'Booking Confirmation'
    message = f'Hey,\n\nBooking done sucessfuly. booking details : {booking_details}'

    send_mail(subject, message, EMAIL_HOST_USER, [email])
    return 'Mail sent successfully'
