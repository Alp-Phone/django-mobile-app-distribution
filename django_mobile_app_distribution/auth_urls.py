# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^login/$',
        auth_views.auth_login,
        {'template_name': 'django_mobile_app_distribution/login.html'},
        name='auth_login'),
    url(r'^logout/$',
        auth_views.auth_logout,
        {'template_name': 'django_mobile_app_distribution/logout.html'},
        name='auth_logout'),
]
