from django.db import models

class Relatives(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    nickname = models.CharField(max_length=30, null=True, blank=True)
