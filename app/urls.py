from django.urls import path
from .views import taillift_tailgate_views

urlpatterns = [
    path('', taillift_tailgate_views.type, name='taillift&tailgate'),
    path('<str:type>', taillift_tailgate_views.size, name='size'),
    path('<str:type>/<str:size>', taillift_tailgate_views.products, name='products'),
    path('<str:type>/<str:size>/<str:product>', taillift_tailgate_views.product_view, name='product_view'),
]