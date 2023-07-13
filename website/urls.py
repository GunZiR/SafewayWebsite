"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

from app.views import views


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('rosetta/', include('rosetta.urls')),
    re_path(r'^i18n/', include('django.conf.urls.i18n')),
    path('about-us', views.about_us, name='about_us'),
    path('contact-us', views.contact_us, name='contact_us'),
    path('after-sales-service', views.after_sales_service, name='after_sales_service'),
    path('warranty', views.warranty, name='warranty'),
    path('onsite-services', views.onsite, name='onsite'),
    path('tail-lift-tail-gate/', include('app.urls.taillift_tailgate_urls')),
    path('cooling-system/', include('app.urls.cooling_system_urls')),
    path('logistic-product/', include('app.urls.logistic_product_urls')),
    path('dump-hoist/', include('app.urls.dump_hoist_urls')),
)
