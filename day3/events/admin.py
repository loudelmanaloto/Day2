from django.contrib import admin
from .models import Venue, Attendee, Event

# Register your models here.
admin.site.register(Venue)
admin.site.register(Attendee)
admin.site.register(Event)