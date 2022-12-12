from django.shortcuts import render
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView

from .serializers import *
from .models import *

# Create your views here.

class MovieView(ListCreateAPIView):

    queryset=Movie.objects.all()
    serializer_class = MovieSerializer


class MovieViewDetail(RetrieveUpdateDestroyAPIView):

    queryset=Movie.objects.all()
    serializer_class = MovieSerializer