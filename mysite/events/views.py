from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base.html')

def all_venues(request):
    name = "Loudel Manaloto"
    return render(request, 'venues.html', {'name': name})

def upload_file(request, form):
    #logic checking file format
    pass