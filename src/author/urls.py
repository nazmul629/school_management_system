from django.urls import path
from .views import *

urlpatterns = [
    path('auth_register/',register, name="register"),
    path('auth_login/',userlogin, name='login'),
    path('auth_logout/',userlogout,name='logout')

]