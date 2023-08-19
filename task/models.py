from django.db import models
from account.models import CustomUser


TASK_MODEL_STATUS_CHOICES = [
    (1, "TODO"),
    (2, "IN_PROGRESS"),
    (3, "DONE"),
]

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TimeField(null=True, blank=True)
    status = models.IntegerField(choices=TASK_MODEL_STATUS_CHOICES,
                                 default=1, null=False,
                                 verbose_name="Task Status")
    assigned_user = models.ForeignKey(to=CustomUser,
                                      on_delete=models.PROTECT,
                                      verbose_name="Assigned User")
    is_deleted = models.BooleanField(verbose_name="Is Deleted",
                                    default=False, null=False)