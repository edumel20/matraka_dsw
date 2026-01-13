"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path

import shared.views
import users.views

urlpatterns = [path('i18n/', include('django.conf.urls.i18n'))] + i18n_patterns(
    path('', lambda r: render(r, 'index.html'), name='index'),
    path('setlang/<str:langcode>/', shared.views.setlang, name='setlang'),
    path('admin/', admin.site.urls),
    path('__reload__/', include('django_browser_reload.urls')),
    path('posts/', include('posts.urls')),
    path('accounts/', include('accounts.urls')),
    path('django-rq/', include('django_rq.urls')),
    path('api/auth/', users.views.auth, name='auth'),
)
