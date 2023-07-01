from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from ..forms import SubmitForm

# Create your views here.
def index(request):
    return render(request, 'app\index.html')

def contact_us(request):
    if request.method == "GET":
        form = SubmitForm()
        print('create form')
    else:
        form = SubmitForm(request.POST)
        print('submit form')
        if form.is_valid():
            print('form valid')
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, ["safeway-email"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return HttpResponse(f"{name}: {email} send with subject '{subject}' and message '{message}'")
        print('invalid form')
    return render(request, 'app\contact_us.html', {"form": form})

def about_us(request):
    return render(request, 'app\about_us.html')

def after_sales_service(request):
    return render(request, 'app\after_sales_service.html')