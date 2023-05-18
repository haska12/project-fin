from django.core.mail import send_mail
from django.conf import settings
import uuid

def send_forget_password(email,token,pk):

    token
    subject="you forget your password"
    message=f'here to reste your password http://127.0.0.1:8000/rest_password/{token}/{pk} '
    from_email=settings.EMAIL_HOST_USER
    recipient_list=[email]
    print(message)
    # start email host server for test only
    # python -m smtpd -n -c DebuggingServer localhost:587

    #send_mail(subject,message,from_email,recipient_list)
    return True



