from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import requires_csrf_token
from . import ml_predict
# Create your views here.

def index(request):
    return render(request, 'app/index.html')


def result(request):  
    pclass = int(request.GET['pclass'])
    
    sex = request.GET['sex']
    if  sex == "male":
        sexVal = 0
    else:
        sexVal = 1
        
    age = int(request.GET['age'])
    
    sibsp = int(request.GET['sibsp'])
    parch = int(request.GET['parch'])
    fare = int(request.GET['fare'])
    
    embarked = request.GET['embarked']
    if embarked == "s":
        embarkedVal = 0
    elif embarked == "c":
        embarkedVal = 1
    elif embarked == "q":
        embarkedVal = 2
        
    title = int(request.GET['title']) 
          
    
    output = ml_predict.prediction_model(pclass, sexVal,age, sibsp, parch, fare, embarkedVal, title)
    return render(request, 'app/result.html', {'home_input':output })