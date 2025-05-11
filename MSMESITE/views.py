from django.shortcuts import render
import json
from django.http import JsonResponse
from urllib.parse import unquote
def index(request):
    return render(request, 'index.html')

def SCHEMES(request):
    # with open('static/data/minslist.txt', 'r') as file:
    #     SCHEMESLIST = file.readlines()
    with open('static/data/msme.json', 'r') as file:
        data = json.load(file)
    SCHEMESLIST=[sche for sche in data['Scheme']]
    
    return render(request, 'schems.html',{"SCHEMESLIST": SCHEMESLIST})


# def register_scheme(request, scheme):
#     # Do something with the scheme
#     print("User selected scheme:", scheme)

#     return render(request, 'schems.html',{"SCHEMESLIST": scheme})


def register_scheme(request,scheme):
  
    
            
            with open('static/data/test.json', 'r') as file:
                 data = json.load(file)
            
            
            # print(scheme)
            # scheme = unquote(scheme)
            scheme = unquote(scheme)
            request.session["schems"] = scheme
        
            SCHEMESLIST=[sche for sche in data['Scheme'][scheme]]
            
           
            return render(request, 'mainscheme.html',{"SCHEMESLIST": SCHEMESLIST})


 
def nanmainpage(request,scheme):
  
            with open('static/data/test.json', 'r') as file:
                 data = json.load(file)
            
    
            
            scheme = unquote(scheme)
            request.session["subsubscheme"] = scheme
            subscheme =  request.session.get("SubScmens")
            subsubscheme = request.session.get("subsubscheme")
            # print(scheme)
            MainSchems = request.session.get("MainSchems")
            
            SCHEME = request.session.get("schems")
            
            SCHEMESLIST= data['Scheme'][SCHEME][MainSchems][subscheme][subsubscheme]
          
            return render(request, 'mainpage.html',{'scheme': SCHEMESLIST})

         
def mainpage(request,scheme):
  
            with open('static/data/test.json', 'r') as file:
                 data = json.load(file)
            
    
            
            scheme = unquote(scheme)
            request.session["subsubscheme"] = scheme
            subscheme =  request.session.get("SubScmens")
            subsubscheme = request.session.get("subsubscheme")
            # print(scheme)
            MainSchems = request.session.get("MainSchems")
            # print(subsubscheme)
            SCHEME = request.session.get("schems")
            # print([key for key in data['Scheme'][SCHEME][MainSchems][subscheme]])
            SCHEMESLIST= data['Scheme'][SCHEME][MainSchems][subscheme][subsubscheme]
            
      
            return render(request, 'mainpage.html',{'scheme': SCHEMESLIST,"schemename":subsubscheme})

def subsubscheme(request,scheme):
  
            with open('static/data/test.json', 'r') as file:
                 data = json.load(file)
            
    
            
            scheme = unquote(scheme)
            request.session["SubScmens"] = scheme
            MainSchems = request.session.get("MainSchems")
            SCHEME = request.session.get("schems")
            SCHEMESLIST=[sche for sche in data['Scheme'][SCHEME][MainSchems][scheme]]
            # print(SCHEMESLIST)
            if 'NaN' in SCHEMESLIST:
                # print(SCHEMESLIST)
                SCHEMESLIST= data['Scheme'][SCHEME][MainSchems][scheme]['NaN']
                # print(SCHEMESLIST)
                return render(request, 'mainpage.html',{'scheme': SCHEMESLIST,"schemename":scheme})
            return render(request, 'subsubscheme.html',{"SCHEMESLIST": SCHEMESLIST})


def SUB_SCHEMES(request,scheme):
  
            with open('static/data/test.json', 'r') as file:
                 data = json.load(file)
            
    
            
            scheme = unquote(scheme)
            request.session["MainSchems"] = scheme
         
            SCHEME = request.session.get("schems")
           
            SCHEMESLIST=[sche for sche in data['Scheme'][SCHEME][scheme]]
            # print(SCHEMESLIST)
            if 'NaN' in SCHEMESLIST:
                # print(SCHEMESLIST)
                SCHEMESLIST= data['Scheme'][SCHEME][scheme]['NaN']['NaN']
          
                return render(request, 'mainpage.html',{'scheme': SCHEMESLIST,"schemename":scheme})
            return render(request, 'subscheme.html',{"SCHEMESLIST": SCHEMESLIST})
