from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mostrarHtml(request):
    return HttpResponse('<h1>appProva</h1>')

def home(request):
    return render(request, 'home.html')