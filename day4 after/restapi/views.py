from django.shortcuts import render

from .serializers import EventSerializer
from rest_framework import viewsets
from events.models import Event


# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer