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

# def contact(request):
#     # if request.method == "POST":
#     #     name = request.POST['name']
#     #     email = request.POST['email']
#     #     subject = request.POST['subject']
#     #     message = request.POST['message']
#     #
#     #     ob = Contact(name=name, email=email, contact=contact,
#     #                  subject=subject)
#     #     ob.save()
#     #     return redirect('contact')
#
#     return render(request, 'contact.html')


def service(request):
    return render(request, 'services.html')


def starter(request):
    return render(request, 'starter-page.html')
