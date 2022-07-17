from datetime import datetime

from django.db import models

# Create your models here.
from join.models import Member


class Rboard(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.ForeignKey(Member, on_delete=models.DO_NOTHING)
    workjum = models.IntegerField(default=0)
    supjum = models.IntegerField(default=0)
    regdate = models.DateTimeField(default=datetime.now)
    contents = models.TextField()

    class Meta:
        db_table = 'rboard'
        ordering = ['-id']

class Info(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    member = models.TextField()
    e_add = models.TextField()
    regdate = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'Info'
        ordering = ['-id']

