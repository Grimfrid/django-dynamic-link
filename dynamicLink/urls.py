# -*- coding:utf-8 -*-
# This Python file uses the following encoding: utf-8

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('', 
                       (url(r'^site/([\w-]*)/$', 'dynamicLink.views.site')),
                       (url(r'^link/(\w{1,100})/.*$', 'dynamicLink.views.fetch')),
                       (url(r'^link/(\w{1,100})$', 'dynamicLink.views.fetch')), # without prefix
                       )
