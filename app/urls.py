from django.urls import path, include
from .views import tailgate_views

urlpatterns = [
    path('', tailgate_views.index, name='tail-lift_index'),
    path('<str:type>', tailgate_views.tailgate, name='tailgate'),
]