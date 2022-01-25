from django.shortcuts import render
from random import randint

def games_home(request):
    return render(request, 'games/games_home.html')

