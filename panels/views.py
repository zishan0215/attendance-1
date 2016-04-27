from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def forms(request):
    return render(request, 'forms.html')

def tables(request):
    return render(request, 'tables.html')

def forgot_password(request):
    return render(request, 'forgot_password.html')