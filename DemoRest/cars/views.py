from django.shortcuts import render
from rest_framework import generics
from cars.serializers import *
from cars.models import *
from cars.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication, SessionAuthentication


class CarListView(generics.ListAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
    authentication_classes = (TokenAuthentication, SessionAuthentication)