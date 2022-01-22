from django.shortcuts import render
from random import randint
from time import sleep


# Create your views here.

def games_home(request):
    return render(request, 'games/games_home.html')

