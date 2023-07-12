from django.shortcuts import render, get_object_or_404

from ..models import (TailGateTailLift,
                      CoolingSystem,
                      LogisticProduct,
                      DumpHoist,
                      Accessory,
                      AccessoriesStatus)

def TailLiftTailGateView(request, path=None):
    content = {}
    if path:
        args_list = path.split('/')
        name = args_list[-1]
        node = get_object_or_404(TailGateTailLift, name=name)
        content['header'] = name.split(' ')
        products = node.get_children()
        last = node.get_last_child()
        content['last'] = last.name
    else:
        content['header'] = ['Tail Gate', ' & Tail Lift']
        products = TailGateTailLift.objects.all()
    content['products'] = products
    return render(request, 'product\\tl&tg_product.html', content)

def AccessoryView(request, type):
    accessory_status = get_object_or_404(AccessoriesStatus, name__name=type)
    accessories = list()
    fields = accessory_status._meta.get_fields()
    for field in fields:
        if field.name != 'id' and field.name != 'name':
            if getattr(accessory_status, field.name):
                accessories.append(Accessory.objects.get(name=field.verbose_name))
    content = {'header': type.split(' '), 'accessories': accessories}
   
    return render(request, 'product\\accessory.html', content)
    

def CoolingSystemView(request, path=None):
    content = {}
    if path:
        args_list = path.split('/')
        name = args_list[-1]
        node = get_object_or_404(CoolingSystem, name=name)
        content['header'] = name.split(' ')
        products = node.get_children()
    else:
        content['header'] = ['Cooling', ' System']
        products = CoolingSystem.objects.all()
    content['products'] = products
    return render(request, 'product\\product.html', content)


def LogisticProductView(request, path=None):
    content = {}
    if path:
        args_list = path.split('/')
        name = args_list[-1]
        node = get_object_or_404(LogisticProduct, name=name)
        content['header'] = name.split(' ')
        products = node.get_children()
    else:
        content['header'] = ['Logistic', ' Product']
        products = LogisticProduct.objects.all()
    content['products'] = products
    return render(request, 'product\\product.html', content)


def DumpHoistView(request, path=None):
    content = {}
    if path:
        args_list = path.split('/')
        name = args_list[-1]
        node = get_object_or_404(DumpHoist, name=name)
        content['header'] = name.split(' ')
        products = node.get_children()
    else:
        content['header'] = ['Dump', ' Hoist']
        products = DumpHoist.objects.all()
    content['products'] = products
    return render(request, 'product\\product.html', content)