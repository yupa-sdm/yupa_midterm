from django.shortcuts import render, HttpResponse

# Create your views here.
def หน้าแรก(request):
    return render(request, 'หน้าแรก.html')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')