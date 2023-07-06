from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages

from ..forms import SubmitForm

# Create your views here.
def index(request):
    return render(request, 'app\index.html')

def contact_us(request):
    if request.method == 'POST':
        form = SubmitForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry" 
            body = {
                'name': form.cleaned_data["name"],
                'email': form.cleaned_data["email"],
                'subject': form.cleaned_data["subject"],
                'message': form.cleaned_data['message']
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, '63010391@kmitl.ac.th', ['63010391@kmitl.ac.th']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, "Message sent." )
            return redirect ("contact_us")
    form = SubmitForm()
    return render(request, 'app\\contact_us.html', {"form": form})

def about_us(request):
    return render(request, 'app\\about_us.html')

def after_sales_service(request):
    return render(request, 'app\\after_sales_service.html')