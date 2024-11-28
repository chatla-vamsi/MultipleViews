from django.urls import path

from app4.views import *

urlpatterns=[
    path('',home),
    path('login/',login_page),
]