import email
from django.shortcuts import render
import requests
from django.contrib import messages

REGISTER_URL = 'http://127.0.0.1:8000/api/accounts/register/'
# Create your views here.
def RegisterationView(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        data = {
            "username":username,
            "email":email,
            "password":password,
            "password2":password2
        }
        response = requests.post(REGISTER_URL,data)
        json_respose= response.json()
        print(response)
        print(json_respose)
        
        status = json_respose['response']
        
        if status == "FAILED":
            messages.error(request,str(json_respose))
        else:
            messages.success(request,"Success")
 
            
    
        
    return render(request,'registeration.html')