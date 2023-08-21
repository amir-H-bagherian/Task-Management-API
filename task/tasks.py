import os
from celery import Celery, shared_task
from django.core.mail import send_mail
from core.settings import EMAIL_HOST_USER

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
app = Celery('tasks')
app.config_from_object("task.celeryconfig")
app.autodiscover_tasks()


@shared_task
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
        return {"msg": "Sent successfully"}
    except Exception as e:
        return {"msg": e.args}