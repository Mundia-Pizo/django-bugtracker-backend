from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Project, Tracker
from .serializers import ProjectAPIViewSerializer, TrackerAPIViewSerializer
from rest_framework import permissions, viewsets


class ProjectView(ListCreateAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectAPIViewSerializer
	permission_classes=[
      permissions.AllowAny
	]

	def perform_create(self, *args, **kwargs):
		pass


class TrackerView(viewsets.ModelViewSet):
	queryset = Tracker.objects.all()
	permission_classes= [
       permissions.AllowAny]
	serializer_class = TrackerAPIViewSerializer

	def perform_create(self,request,*args, **kwargs):
		pass
