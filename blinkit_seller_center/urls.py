"""
URL configuration for blinkit_seller_center project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from products.soap import product_soap_service
from orders.soap import order_soap_service
from inventory.soap import inventory_soap_service
from catalog.soap import catalog_soap_service
from seller.soap import seller_soap_service
from analytics.soap import analytics_soap_service

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # REST API endpoints
    path('api/', include('products.urls')),
    path('api/', include('orders.urls')),
    path('api/', include('inventory.urls')),
    path('api/', include('catalog.urls')),
    path('api/', include('seller.urls')),
    path('api/', include('analytics.urls')),
    
    # SOAP API endpoints
    path('soap/products/', product_soap_service, name='product_soap'),
    path('soap/orders/', order_soap_service, name='order_soap'),
    path('soap/inventory/', inventory_soap_service, name='inventory_soap'),
    path('soap/catalog/', catalog_soap_service, name='catalog_soap'),
    path('soap/seller/', seller_soap_service, name='seller_soap'),
    path('soap/analytics/', analytics_soap_service, name='analytics_soap'),
]
