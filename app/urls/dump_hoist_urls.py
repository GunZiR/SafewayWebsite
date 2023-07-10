from django.urls import path

from ..views import product_views

urlpatterns = [
    path('', product_views.DumpHoistView, name='dump_hoist_index'),
    path('<path:path>', product_views.DumpHoistView, name='dump_hoist_product'),
]