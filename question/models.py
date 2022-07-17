from datetime import datetime

from django.db import models

# Create your models here.
from join.models import Member


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    qname =models.ForeignKey(Member, on_delete=models.DO_NOTHING)
    qphone = models.CharField(max_length=16)
    qemail = models.CharField(max_length=40)
    qselect = models.CharField(max_length=20)
    qsubject = models.TextField()
    context = models.TextField()
    regdate = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'question'
        ordering = ['-id']
