from django.urls import path

from app1.views import *

urlpatterns=[
    path('',home),
    path('login/',login_page),
]