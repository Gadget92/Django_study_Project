from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def home2(request, month):
    return render(request, 'home.html', {})

def home2(request, month, year):
    return render(request, 'home.html', {})
