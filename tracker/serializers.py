from rest_framework import serializers
from .models import  Project, Tracker


class ProjectAPIViewSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields='__all__'



class TrackerAPIViewSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tracker
		fields = '__all__'