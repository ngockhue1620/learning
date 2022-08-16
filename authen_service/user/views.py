from rest_framework import viewsets, status
from .serializers import UserSerializer
from rest_framework.decorators import action 
from django.contrib.auth.models import User
from rest_framework.response import Response


class LoginViewset(viewsets.ViewSet):

  @action(methods= ['POST'],  detail=False, url_path="login", permission_classes=[] )
  def login(self, request):
    user = User.objects.all().first()
    serializer = UserSerializer(user)
    return Response(serializer.data, status= status.HTTP_200_OK)