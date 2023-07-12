from django.urls import path

from ..views import product_views

urlpatterns = [
    path('', product_views.TailLiftTailGateView, name='tl&tg_index'),
    path('<str:type>/accessory', product_views.AccessoryView, name='tl&tg_accessory'),
    path('<path:path>', product_views.TailLiftTailGateView, name='tl&tg_product'),
]