from django.shortcuts import render

def education(request):
    return render(request, 'education/education.html')
def school(request):
    return render(request, 'education/school.html')
def university(request):
    return render(request, 'education/university.html')
def library(request):
    return render(request, 'education/library.html')
def science(request):
    return render(request, 'education/science.html')
