"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
import rest_framework
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

from rest_framework.routers import SimpleRouter
from views import ApplicationViewSet,ModuleViewSet,SheetViewSet


router = SimpleRouter()
router.register('applications',ApplicationViewSet,'application')
router.register('modules',ModuleViewSet,'module')
router.register('sheets',SheetViewSet,'sheet')

urlpatterns = [
    # url(r'^applications/$', RedisTestView.as_view(),name='applications'),
    # url(r'^applications/$', RedisTestView.as_view(),name='applications'),
    # url(r'^applications/(?P<pk>[0-9]{1,10})/modules/$', RedisTestView.as_view(),name='applications'),
	url(r'^main/$',login_required(TemplateView.as_view(template_name='webapi/mainwindow.html'),),name='webapi-main'),

]


urlpatterns += router.urls