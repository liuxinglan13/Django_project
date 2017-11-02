"""maoyan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^movie/', include('movie.urls', namespace='movie', app_name='movie')),
    url(r'^tskr/', include('tskr.urls', namespace='tskr', app_name='tskr')),
    url(r'^tangshi/', include('tangshi.urls', namespace='tangshi', app_name='tangshi')),
    url(r'^weekreport/', include('weekreport.urls', namespace='weekreport', app_name='weekreport')),
    url(r'^codetest/', include('codetest.urls', namespace='codetest', app_name='codetest')),
]
