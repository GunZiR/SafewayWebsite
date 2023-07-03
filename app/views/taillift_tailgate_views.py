from django.shortcuts import render

def type(response):
    content = {'types': ['Tail Lift', 'Van Lift', 'Tail Gate', 'Step Frame']}
    return render(response, 'taillift-tailgate\\type.html', content)

def size(response, type):
    content = {'type': type, 'sizes': ['trailer', '10 wheels', 'small 6 wheels', 'big 6 wheels', 'big 4 wheels', 'pickup']}
    return render(response, 'taillift-tailgate\\size.html', content)

def products(response, type, size):
    if size=='trailer':
        content = {'type': type, 'size': size, 'products': ['trailer 1', 'trailer 2', 'trailer 3']}
    elif size=='10 wheels':
        content = {'type': type, 'size': size, 'products': ['10 wheels 1', '10 wheels 2', '10 wheels 3']}
    elif size=='small 6 wheels':
        content = {'type': type, 'size': size, 'products': ['small 6 wheels 1', 'small 6 wheels 2', 'small 6 wheels 3']}
    elif size=='big 6 wheels':
        content = {'type': type, 'size': size, 'products': ['big 6 wheels 1', 'big 6 wheels 2', 'big 6 wheels 3']}
    elif size=='big 4 wheels':
        content = {'type': type, 'size': size, 'products': ['big 4 wheels 1', 'big 4 wheels 2', 'big 4 wheels 3']}
    elif size=='pickup':
        content = {'type': type, 'size': size, 'products': ['pickup', 'box', 'carryboy']}
    else:
        return render(response, 'app\\404.html')

    return render(response, 'taillift-tailgate\\products.html', content)

def product_view(response, type, size, product):
    if product=='pickup':
        content = {'type': type, 'size': size, 'product': product, 'choices': ['SWA600S', 'Accessory']}
    elif product=='box':
        content = {'type': type, 'size': size, 'product': product, 'choices': ['SWA600S', 'Accessory']}
    elif product=='carryboy':
        content = {'type': type, 'size': size, 'product': product, 'choices': ['SWA600S', 'SWA600S', 'Accessory']}
    else:
        return render(response, 'app\\404.html')
    
    return render(response, 'taillift-tailgate\\product_view.html', content)
