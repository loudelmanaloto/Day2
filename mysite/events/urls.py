from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="Index page"),
    path('venues', views.all_venues, name="Venue Page")
]