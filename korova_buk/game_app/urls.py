from django.urls import path
from .views import *

urlpatterns = [
    path('', UserInput, name = 'game'),
]
