from django.urls import path

from ..views import product_views

urlpatterns = [
    path('', product_views.LogisticProductView, name='logistic_product_index'),
    path('<path:path>', product_views.LogisticProductView, name='logistic_product'),
]