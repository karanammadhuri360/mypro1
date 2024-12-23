from django.shortcuts import render

# Create your views here.

def home(request):
    v='New Home page'
    return render(request,'home.html',{'data':v})
 
def login(request):
    return render(request,'login.html')
 
def signup(request):
    return render(request,'signup.html')

def update(request):
    return render(request,'update.html')

def delete(request):
    return render(request,'delete.html')






