from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', MovieView.as_view(),name='movies_api'),
    path('<pk>', MovieViewDetail.as_view(),name='movies_detail'),
]