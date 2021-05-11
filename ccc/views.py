from django.shortcuts import render, redirect
from .forms import ContactForm 
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def team(request):
    return render(request, 'team.html', {})

def portfolio(request):
    return render(request, 'portfolio.html', {})

def recruitment(request):
    return render(request, 'recruitment.html', {})

def services(request):
    return render(request, 'services.html', {})

def contact(request):
    form = ContactForm()
    if request.method =='POST':
        form = ContactForm(request.POST)

    if form.is_valid():
        subject = f'Message from {form.cleaned_data["first_name" + "last_name"]}'
        message = form.cleaned_data["message"]
        sender = form.cleaned_data["email"]
        phone = form.cleaned_data["phone"]
        company = form.cleaned_data["company"]
        recipients = ["ucsdcornerstone@gmail.com"]
        try:
            send_mail(subject, message, sender, phone, company, recipients, fail_silently = True)
        except BadHeaderError:
            return HttpResponse('Invalid Header Found')
        return HttpResponse('Success...Your email has been sent.')

    return render(request, 'contact.html', {'form': form })