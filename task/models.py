from django.db import models
from account.models import CustomUser
from task import tasks

TASK_MODEL_STATUS_CHOICES = [
    (1, "TODO"),
    (2, "IN_PROGRESS"),
    (3, "DONE"),
]

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=TASK_MODEL_STATUS_CHOICES,
                                 default=1, null=False,
                                 verbose_name="Task Status")
    assigned_user = models.ForeignKey(to=CustomUser,
                                      on_delete=models.PROTECT,
                                      verbose_name="Assigned User")
    is_deleted = models.BooleanField(verbose_name="Is Deleted",
                                    default=False, null=False)
    def __str__(self) -> str:
        return '{} - {}'.format(self.title, self.assigned_user.get_full_name())
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.status == 3: # if Task is done
            e = tasks.send_email_to_user.delay(
                task_title=self.title,
                email=self.assigned_user.email
            )
            print('e:', e)
            print('status of e:', e.status)