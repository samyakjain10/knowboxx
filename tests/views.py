from django.shortcuts import render

# Create your views here.
def testspage(request):
    return render(request, 'test/test.html')