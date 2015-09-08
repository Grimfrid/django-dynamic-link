#!/usr/bin/python
# -*- coding:utf-8 -*-
# This Python file uses the following encoding: utf-8

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# This file holds the presettings of the app. 

# A path to a directory from witch walk down so you can choose your files.
DYNAMIC_LINK_MEDIA = getattr(settings, 'DYNAMIC_LINK_MEDIA', settings.MEDIA_ROOT)

# A string that modify the serve url path:
# /www.example.com/DYNAMIC_LINK_URL_BASE_COMPONENT/link/3839hd8HKl3/example.zip
DYNAMIC_LINK_URL_BASE_COMPONENT = getattr(settings, 'DYNAMIC_LINK_URL_BASE_COMPONENT', 'serve')

# It's here because of not violate the DRY priciple.
TEXT_REQUEST_DOES_NOT_EXIST = _(u'This request is faulty')
TEXT_REQUEST_IS_EXPIRED = _(u'Sorry, this request is already expired')