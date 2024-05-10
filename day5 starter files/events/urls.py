from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    # path('events/', views.show_events, name="event-list"),
    # path('venues/', views.show_venues, name="venue-list"),
    # path('members/', views.show_members, name="member-list"),

    path('events/', views.EventListView.as_view(), name="event-list"),
    path('venues/', views.VenueListView.as_view(), name="venue-list"),
    path('members/', views.AttendeeListView.as_view(), name="member-list"),

    path('newevent/', views.EventCreateView.as_view(), name="add-event"),
    path('newvenue/', views.VenueCreateView.as_view(), name="add-venue"),
    path('newmember/', views.AttendeeCreateView.as_view(), name="add-member"),

    path('events/<slug:pk>', views.EventDetailView.as_view(), name="show-event"),
    path('venues/<slug:pk>', views.VenueDetailView.as_view(), name="show-venue"),
    path('members/<slug:pk>', views.AttendeeDetailView.as_view(), name="show-member"),


    path('editevent/<slug:pk>', views.EventUpdateView.as_view(), name="edit-event"),
    path('editvenue/<slug:pk>', views.VenueUpdateView.as_view(), name="edit-venue"),
    path('editmember/<slug:pk>', views.AttendeeUpdateView.as_view(), name="edit-member"),
    
    path('deleteevent/<slug:pk>', views.EventDeleteView.as_view(), name="delete-event"),
    path('deletevenue/<slug:pk>', views.VenueDeleteView.as_view(), name="delete-venue"),
    path('deletemember/<slug:pk>', views.AttendeeDeleteView.as_view(), name="delete-member"),

]
