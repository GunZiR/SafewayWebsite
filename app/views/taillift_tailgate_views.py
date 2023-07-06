from django.shortcuts import render

def type(request):
    content = {'types': ['Tail Lift', 'Van Lift', 'Tail Gate', 'Step Frame']}
    return render(request, 'taillift-tailgate\\type.html', content)

def size(request, type):
    content = {'type': type, 'sizes': ['trailer', '10 wheels', 'small 6 wheels', 'big 6 wheels', 'big 4 wheels', 'pickup']}
    return render(request, 'taillift-tailgate\\size.html', content)

def box(request, type, size):
    if size=='trailer':
        content = {'type': type, 'size': size, 'boxes': ['trailer 1', 'trailer 2', 'trailer 3']}
    elif size=='10 wheels':
        content = {'type': type, 'size': size, 'boxes': ['10 wheels 1', '10 wheels 2', '10 wheels 3']}
    elif size=='small 6 wheels':
        content = {'type': type, 'size': size, 'boxes': ['small 6 wheels 1', 'small 6 wheels 2', 'small 6 wheels 3']}
    elif size=='big 6 wheels':
        content = {'type': type, 'size': size, 'boxes': ['big 6 wheels 1', 'big 6 wheels 2', 'big 6 wheels 3']}
    elif size=='big 4 wheels':
        content = {'type': type, 'size': size, 'boxes': ['big 4 wheels 1', 'big 4 wheels 2', 'big 4 wheels 3']}
    elif size=='pickup':
        content = {'type': type, 'size': size, 'boxes': ['pickup', 'box', 'carryboy']}
    else:
        return render(request, 'app\\404.html')

    return render(request, 'taillift-tailgate\\box.html', content)

def product(request, type, size, box):
    if box=='pickup':
        content = {'type': type, 'size': size, 'box': box, 'products': ['SWA600S', 'Accessory']}
    elif box=='box':
        content = {'type': type, 'size': size, 'box': box, 'products': ['SWA600S', 'Accessory']}
    elif box=='carryboy':
        content = {'type': type, 'size': size, 'box': box, 'products': ['SWA600S', 'SWA600S', 'Accessory']}
    else:
        return render(request, 'app\\404.html')
    
    return render(request, 'taillift-tailgate\\product.html', content)
