from django import forms 
from django.forms import ModelForm
from .models import Venue, Attendee, Event


class VenueForm(ModelForm):
    class Meta: #allows you to define things in class in django
        model = Venue
        # fields = "__all__" # if you want all
        fields = ('name', 'address', 'zip_code', 'web') # define each fields

        labels = {
            'name': '',
            'address': '',
            'zip_code': '',
            'web':''
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Venue Name'}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
            'zip_code': forms.TextInput(attrs={'class':'form-control','placeholder':'Zip Code'}),
            'web': forms.TextInput(attrs={'class':'form-control','placeholder':'Website URL'})
        }

class EventForm(ModelForm):
    class Meta: #allows you to define things in class in django
        model = Event
        # fields = "__all__" # if you want all
        fields = ('name', 'venue', 'event_date', 'manager', 'description', 'attendees') # define each fields

        labels = {
            'name': '',
            'venue': '',
            'event_date': '',
            'manager':'',
            'description':'',
            'attendees':''
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Event Name'}),
            'venue': forms.Select(attrs={'class':'form-control','placeholder':'Venue'}),
            'event_date': forms.TextInput(attrs={'class':'form-control','placeholder':'Event Date'}),
            'manager': forms.TextInput(attrs={'class':'form-control','placeholder':'Manager'}),
            'description': forms.TextInput(attrs={'class':'form-control','placeholder':'Description'}),
            'attendees': forms.SelectMultiple(attrs={'class':'form-control','placeholder':'Attendees'}),
        }

