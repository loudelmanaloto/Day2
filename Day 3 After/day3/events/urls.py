from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('events/', views.events, name="events-list"),
    # path('venues/', views.venues, name="venues-list"),
    path('venues/', views.VenueListView.as_view(), name="venues-list"),
    path('venues/add', views.VenueCreateView.as_view(), name="add-venue"),
    path('venues/<slug:pk>', views.VenueDetailView.as_view(), name="show-venue"),
    

]
