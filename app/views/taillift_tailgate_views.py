from django.shortcuts import render
from django.http import Http404

# from ..models import TailGateTailLift

def type(request):
    return render(request, 'taillift-tailgate\\type.html')

def size(request, type):
    return render(request, 'taillift-tailgate\\size.html')

def box(request, type, size):
    return render(request, 'taillift-tailgate\\box.html')

def product(request, type, size, box):
    return render(request, 'taillift-tailgate\\product.html')
