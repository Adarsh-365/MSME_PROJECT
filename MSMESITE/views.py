from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def SCHEMES(request):
    with open('static/data/minslist.txt', 'r') as file:
        SCHEMESLIST = file.readlines()
    
    return render(request, 'schems.html',{"SCHEMESLIST": SCHEMESLIST})