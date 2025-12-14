from django.shortcuts import render
from .models import Novosti



def index(request):
    return render(request, 'main/index.html')
def posetitelam(request):
    news = Novosti.objects.order_by('date')
    return render(request, 'main/posetitelam.html', {'news': news})
def contacts(request):
    return render(request, 'main/contacts.html')
def education(request):
    return render(request, 'main/education.html')
def programs(request):
    return render(request, 'main/programms.html')
def store(request):
    return render(request, 'main/store.html')
def always(request):
    return render(request, 'main/always.html')
def temporary(request):
    return render(request, 'main/temporary.html')
def online(request):
    return render(request, 'main/online.html')
