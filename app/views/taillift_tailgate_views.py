from django.shortcuts import render, get_object_or_404

from ..models import TailGateTailLift

def type(request):
    types = TailGateTailLift.objects.all()
    content = {'types': types}
    return render(request, 'taillift-tailgate\\type.html', content)

def size(request, type):
    content = {'header': type.split(' '), 'type': type}
    node = get_object_or_404(TailGateTailLift, name=type)
    sizes = node.get_children()
    content['sizes'] = sizes
    return render(request, 'taillift-tailgate\\size.html', content)

def box(request, type, size):
    content = {'header': size.split(' '), 'type': type, 'size': size}
    node = get_object_or_404(TailGateTailLift, name=size)
    boxes = node.get_children()
    content['boxes'] = boxes
    return render(request, 'taillift-tailgate\\box.html', content)

def product(request, type, size, box):
    content = {'header': box.split(' '), 'type': type, 'size': size, 'box': box}
    node = get_object_or_404(TailGateTailLift, name=box)
    products = node.get_children()
    content['products'] = products
    return render(request, 'taillift-tailgate\\product.html', content)
