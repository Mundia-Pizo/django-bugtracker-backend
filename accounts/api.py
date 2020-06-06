from .serializers import  (
	UserSerializer,
	 RegisterSerializer,
	  LoginSerializer,
	  )
from rest_framework import permissions, generics
from rest_framework.response import Response
from knox.models import AuthToken
from knox.auth import TokenAuthentication
from rest_framework.authentication import BasicAuthentication

class RegisterAPI(generics.GenericAPIView):
	serializer_class =RegisterSerializer

	def post(self,request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user=serializer.save()

		return Response({
			"user":UserSerializer(user, context=self.get_serializer_context()).data,
			"token":AuthToken.objects.create(user)[1]
			})


class LoginAPI(generics.GenericAPIView):
	serializer_class =LoginSerializer
	
	def post(self,request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid()
		user=serializer.validated_data

		return Response({
			"user":UserSerializer(user, context=self.get_serializer_context()).data,
			"token":AuthToken.objects.create(user)[1]
			})

class UserAPI(generics.RetrieveAPIView):
	permission_classes=[
	permissions.IsAuthenticated
	]
	serializer_class=UserSerializer

	def get_object(self):
		return self.request.user

## the logout API will be done using the knox_views in urls check the urls

