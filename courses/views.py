from django.shortcuts import render
from .models import Courses

def coursespage(request):
    courses = Courses.objects.all()
    context = {'courses': courses}
    return render(request, 'courses/courses.html', context)

def coursetemp(request):
    return render(request, 'courses/course1.html')