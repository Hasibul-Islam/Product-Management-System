"""reyebltex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from products.views import (
	home, 
	order_list,
	product_list,
    ProductCreate,
    OrderCreate,
    Productupdate,
    Orderupdate,
    product_delete,
    order_delete,
    order_update_list,
    product_update_list,
    order_delete_list,
    product_delete_list,
    #costing
    costing_list_update,
    CostingCreate,
    CostingUpdate,
    #yearlyprofit
    profit_list,
    product_analysis

	)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^orders/list/$', order_list, name='orders'),
    url(r'^product/analysis/$', product_analysis, name='product_analysis'),
    url(r'^orders/list/update/$', order_update_list, name='orders-update-list'),
    url(r'^orders/list/delete/$', order_delete_list, name='orders-delete-list'),
    url(r'^products/list/$', product_list, name='products'),
    url(r'^products/list/update/$', product_update_list, name='products-update-list'),
    url(r'^products/list/delete/$', product_delete_list, name='products-delete-list'),
    url(r'^products/create/$', ProductCreate.as_view(), name='product-create'),
    url(r'^orders/create/$', OrderCreate.as_view(), name='order-create'),
    url(r'^products/update/(?P<pk>[\d]+)/$', Productupdate.as_view(), name='product-update'),
    url(r'^orders/update/(?P<pk>[\d]+)/$', Orderupdate.as_view(), name='order-update'),
    url(r'^products/delete/(?P<id>[\d]+)/$', product_delete, name='product-delete'),
    url(r'^orders/delete/(?P<id>[\d]+)/$', order_delete, name='order-delete'),
    #cossting
    url(r'^costing/list/$', costing_list_update, name='costing-list'),
    url(r'^costing/create/$', CostingCreate.as_view(), name='costing-create'),
    url(r'^costing/update/(?P<pk>[\d]+)/$', CostingUpdate.as_view(), name='costing-update'),
    url(r'^profit/list/$', profit_list, name='profit-list'),
    url(r'^accounts/', include('accounts.urls'))
]
