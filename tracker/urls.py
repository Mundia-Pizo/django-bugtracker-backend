from django.urls import path, include
from .views import ProjectView, TrackerView
from rest_framework import routers


router = routers.DefaultRouter()
router.register('', TrackerView, 'tracker')
urlpatterns=router.urls