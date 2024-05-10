from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Event, Venue, Attendee
from .forms import VenueForm, EventForm


# Create your views here.
def index(request):
    return render(request, 'base.html', {})

def show_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/events.html', {"object_list":event_list})

def show_venues(request):
    venue_list = Venue.objects.all()
    return render(request, 'events/venues.html', {"object_list": venue_list})

def show_members(request):
    member_list = Attendee.objects.all()
    return render(request, 'events/members.html', {"object_list":member_list})


#class based views
class EventListView(ListView):
    model = Event

class VenueListView(ListView):
    model = Venue

class AttendeeListView(ListView):
    model = Attendee

class EventDetailView(DetailView):
    model = Event


#viewing details of a record
class VenueDetailView(DetailView):
    model = Venue

class AttendeeDetailView(DetailView):
    model = Attendee

class EventCreateView(CreateView):
    model = Event
    # fields = ['name', 'venue', 'event_date', 'manager', 'description', 'attendees']
    form_class = EventForm
    success_url = "/events"


#creating records
class VenueCreateView(CreateView):
    model = Venue
    # fields = ['name', 'address', 'phone', 'web', 'zip_code', 'email_address']
    form_class = VenueForm
    success_url = "/venues"

class AttendeeCreateView(CreateView):
    model = Attendee
    fields = ['first_name', 'last_name', 'email']
    success_url = "/members"


#editing records
class EventUpdateView(UpdateView):
    model = Event
    fields = ['name', 'venue', 'event_date', 'manager', 'description', 'attendees']
    success_url = "/events"


class VenueUpdateView(UpdateView):
    model = Venue
    fields = ['name', 'address', 'phone', 'web', 'zip_code', 'email_address']
    success_url = "/venues"

class AttendeeUpdateView(UpdateView):
    model = Attendee
    fields = ['first_name', 'last_name', 'email']
    success_url = "/members"


#deleting records
class EventDeleteView(DeleteView):
    model = Event
    success_url = '/events'

class VenueDeleteView(DeleteView):
    model = Venue
    success_url = '/venues'

class AttendeeDeleteView(DeleteView):
    model = Attendee
    success_url = '/members'
