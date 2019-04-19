from django.urls import path
from .views import *

urlpatterns = [
    path('',schoolinfo, name='home')

]