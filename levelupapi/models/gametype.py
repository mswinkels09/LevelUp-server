"""GameType model module"""
from django.db import models


class GameType(models.Model):
    """ GameType database model"""

    label = models.CharField(max_length=50)