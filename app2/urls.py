from django.urls import path

from app2.views import *

urlpatterns=[
    path('',home),
    path('login/',login_page),
]