from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from .views import (login_view, register_view, logout_view, change_password)

urlpatterns = [
    url(r'^login/$',login_view, name='login'),
    url(r'^register/$', register_view, name='register'),
    url(r'^password/change/$', change_password, name='change_password'),
    url(r'^logout/$', logout_view, name='logout')
]
