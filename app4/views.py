from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1 style='color:yellow;background-color: black;margin:100px auto; width:200px;padding:20px; border-radius:10px;'>This is app4 home page</h1>")

def login_page(request):
    return HttpResponse("<h1 style='color:white;background-color: blue;margin:100px auto; width:200px;padding:20px; border-radius:10px;'>This is app4 home page</h1>")