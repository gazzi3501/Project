from django.shortcuts import render

def programms(request):
    return render(request, 'programms/programms.html')
def afisha(request):
    return render(request, 'programms/afisha.html')
def lectures(request):
    return render(request, 'programms/lectures.html')
def masterclass(request):
    return render(request, 'programms/masterclass.html')