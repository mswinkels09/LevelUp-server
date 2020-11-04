"""Event model module"""
from django.db import models


class Event(models.Model):
    """ Event database model"""
    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value

    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    day = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    location = models.CharField( max_length=50)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)