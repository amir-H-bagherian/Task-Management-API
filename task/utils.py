from django.core.mail import send_mail
from core.settings import EMAIL_HOST_USER


def send_email_to_user(task_title, email):
    SUBJECT = "Status Changed"
    MESSAGE = f"Task <{task_title}> is now Completed"
    try:
        send_mail(
            subject=SUBJECT,
            message=MESSAGE,
            from_email=EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )
    except:
        pass