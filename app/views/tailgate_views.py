from django.shortcuts import render

# Create your views here.
def tailgate(response):
    return render(response, 'taigate.html')