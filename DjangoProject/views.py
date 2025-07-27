from django.shortcuts import render,redirect
from portfolio.models import  Contact
from django.contrib import messages

def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def gallery(request):
    return render(request, 'gallery.html')


def gallery_single(request):
    return render(request, 'gallery-single.html')


# def contact(request):
#     return render(request, 'contact.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        ob = Contact(name=name, email=email, message=message, subject=subject)
        ob.save()

        messages.success(request, 'Your message has been sent.')
        return redirect('contact-url')

    return render(request, 'contact.html')


def service(request):
    return render(request, 'services.html')


def starter(request):
    return render(request, 'starter-page.html')
