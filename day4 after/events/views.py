from django.shortcuts import render
from .models import Event, Venue

#import django login required decorator

from django.contrib.auth.decorators import login_required

#generic views
from django.views.generic import ListView, DetailView, CreateView


# Create your views here.
def index(request):
    return render(request, 'events/index.html', {})
    
@login_required   
def events(request):
    event_list = Event.objects.all()
    return render(request, 'events/events.html', {"events":event_list})


def venues(request):
    venue_list = Venue.objects.all()
    return render(request, 'events/venues.html', {"venues":venue_list})

class VenueListView(ListView):
    model = Venue
    template_name = 'events/venues.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class VenueDetailView(DetailView):
    model = Venue
    template_name = 'events/venue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class VenueCreateView(CreateView):
    model = Venue
    fields = ['name', 'address', 'zip_code', 'web']
    template_name = "events/addvenue.html"
    success_url = "/venues"

#FBV

