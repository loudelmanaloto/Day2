from django.db import models

# Create your models here.

class Event(models.Model): #classname is your tablename
    name = models.CharField('Events Name',max_length=50)
    event_date = models.DateTimeField('Event Date')
    venue = models.CharField(max_length=120)
    manager = models.CharField(max_length=50)
    description = models.TextField()
    attendees = models.TextField()

    # def __str__(self):
    #     return self.name
