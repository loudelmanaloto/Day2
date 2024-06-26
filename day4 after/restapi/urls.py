from django.urls import path, include
from rest_framework import routers


from . import views


router = routers.DefaultRouter()
router.register(r'events', views.EventViewSet)


urlpatterns = [
      path('', include(router.urls)),
      path('api-auth/', include('rest_framework.urls'), name="rest_framework")
]
