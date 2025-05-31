from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def gallery(request):
    return render(request, 'gallery.html')


def gallery_single(request):
    return render(request, 'gallery-single.html')


def contact(request):
    return render(request, 'contact.html')


def service(request):
    return render(request, 'services.html')


def starter(request):
    return render(request, 'starter-page.html')
