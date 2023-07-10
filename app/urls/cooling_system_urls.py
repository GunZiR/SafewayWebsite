from django.urls import path

from ..views import product_views

urlpatterns = [
    path('', product_views.CoolingSystemView, name='cooling_system_index'),
    path('<path:path>', product_views.CoolingSystemView, name='cooling_system_product'),
]