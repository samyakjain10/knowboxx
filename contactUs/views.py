from django.shortcuts import render
from .models import Contact

# Create your views here.
def contactpage(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        studentclass = request.POST['class']
        message = request.POST['message']

        contact = Contact(name= name, email= email, phone= phone, studentclass=studentclass, message=message)
        contact.save()

    return render(request, 'contactUs/contactus.html')