from django.http import HttpResponse
from django.shortcuts import render

def index (request):
    return render(request, 'index.html')

def analyze (request):

    team1 = request.POST.get('text', 'default')
    team2 = request.POST.get('team2', 'default')
    pitch = request.POST.get('pitch', 'default')
    t1spinners = request.POST.get('t1spinners', 'default')
    t1pacers = request.POST.get('t1pacers', 'default')
    t1allrounders = request.POST.get('t1allrounders', 'default')
    t1captain = request.POST.get('t1captain', 'default')
    t2spinners = request.POST.get('t2spinners', 'default')
    t2pacers = request.POST.get('t2pacers', 'default')
    t2allrounders = request.POST.get('t2allrounders', 'default')
    t2captain = request.POST.get('t2captain', 'default')

    print(team1)
    print(team2)
    return render(request, 'analyze.html')