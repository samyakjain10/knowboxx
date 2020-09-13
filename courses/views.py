from django.shortcuts import render

def coursespage(request):
    return render(request, 'courses/courses.html')

def coursetemp(request):
    return render(request, 'courses/course1.html')