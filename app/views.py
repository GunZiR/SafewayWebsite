from django.shortcuts import render

# Create your views here.
def index(response):
    return render(response, 'index.html')

def contact_us(response):
    return render(response, 'contact_us.html')

def about_us(response):
    return render(response, 'about_us.html')

def after_sales_service(response):
    return render(response, 'after_sales_service.html')