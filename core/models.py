from django.db import models
from django.db.models import Model

class Tasks(Model):
    task = models.TextField()

    class Meta:
        managed = False
        db_table = 'task_list'