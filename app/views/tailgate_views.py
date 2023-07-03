from django.shortcuts import render

def index(response):
    context = {'cars': ['trailer', '10 wheels', 'small 6 wheels', 'big 6 wheels', 'big 4 wheels', 'pick up']}
    return render(response, 'tail-lift\\index.html', context)

def tailgate(response, type):
    return render(response, 'tail-lift\\tailgate.html', {'type': type})

