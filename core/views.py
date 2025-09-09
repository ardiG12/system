from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from core.models import *
from core.serializer import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
