from django.shortcuts import render
from django.http import Http404

from ..models.tail_gate_tail_lift_model import TailGateTailLiftType, TailGateTailLiftSize, TailGateTailLiftBox, TailGateTailLiftProduct

def type(request):
    type = TailGateTailLiftType.objects.all()
    content = {'types': type}
    return render(request, 'taillift-tailgate\\type.html', content)

def size(request, type):
    content = {'header': type.split(' '), 'type': type}
    size = TailGateTailLiftSize.objects.filter(type__name=type)
    if not size.exists():
        raise Http404()
    content['sizes'] = size
    return render(request, 'taillift-tailgate\\size.html', content)

def box(request, type, size):
    content = {'header': size.split(' '), 'type': type, 'size': size}
    box = TailGateTailLiftBox.objects.filter(size__name=size)
    if not box.exists():
        raise Http404()
    content['boxes'] = box
    return render(request, 'taillift-tailgate\\box.html', content)

def product(request, type, size, box):
    content = {'header': box.split(' '), 'type': type, 'size': size, 'box': box}
    product = TailGateTailLiftProduct.objects.filter(box__name=box)
    if not product.exists():
        raise Http404()
    content['products'] = product
    return render(request, 'taillift-tailgate\\product.html', content)
