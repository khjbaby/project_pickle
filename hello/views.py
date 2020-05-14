from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
def home(request):
    name1=request.GET['name']
    age2=request.GET['AGE']
    requestDict=request.GET
    result=int(age2)+7
    requestDict={'result_ohhoo':result}
    return JsonResponse(requestDict)