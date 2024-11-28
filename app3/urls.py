from django.urls import path

from app3.views import *

urlpatterns=[
    path('',home),
    path('login/',login_page),
]