from datetime import datetime

from django.db import models

# Create your models here.
from join.models import Member

# Create your models here.
class Sidonggu(models.Model):
    id = models.AutoField(primary_key=True)
    sido = models.TextField(null=True)
    sigungu = models.TextField(null=True)
    dong = models.TextField(null=True)

    class Meta:
        db_table = 'sidonggu'
        ordering = ['-id']