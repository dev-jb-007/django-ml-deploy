from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from types import SimpleNamespace
import json
from joblib import load
# Create your views here.
@csrf_exempt
def Welcome(request):
    if request.method == 'POST':
        x = json.loads(request.body, object_hook=lambda d: SimpleNamespace(**d))
        temp=x.arr
        model=load('./savedModels/model.joblib')
        y_pred=model.predict([temp])
        print(y_pred)
        if y_pred[0]==0 :
            y_pred='Setosa'
        elif y_pred[0]==1: 
            y_pred='Verscicolor'
        else:
            y_pred='Virginica'
      
        return JsonResponse({'answer':y_pred})
    return JsonResponse({'answer':1})

def User(request):
    username=request.GET['username']
    return render(request,'user.html',{'name':"Dev"})