#!/usr/bin/python
# -*- coding:utf-8 -*-
# This Python file uses the following encoding: utf-8

from django.utils import unittest
from models import Download
from api import DynamicLink

class Obj:
    pass

class DownloadTestCase(unittest.TestCase):
    """Test of the Doanload modell"""
    def setUp(self):
        self.path = '/static/public/testrunner/test.jpg'
        self.file = 'test.jpg'
        self.downl = Download.objects.create(
                              slug='download_model_unittest',
                              file_path=self.path,
                              timeout_hours = 10,
                              max_clicks = 10,
                              )

    def test_download_methodes(self):
        self.assertEqual(self.downl.get_filename(), 
                        self.file,
                        )
        self.assertFalse(self.downl.timeout_clicks())
        self.assertFalse(self.downl.timeout_time())
        self.assertFalse(self.downl.timeout())
        self.assertEqual(self.downl.get_path(), self.path)
    
class DynamicLinkTestCase(unittest.TestCase):
    """Test the DynamicLink API"""
    def setUp(self):
        self.path = '/static/public/testrunner/test.jpg'
        self.file = 'test.jpg'
        self.dlink = DynamicLink(
                      slug='api_unittest',
                      file_path=self.path,
                      timeout_hours = 10,
                      max_clicks = 10,
                      )

    def test_dynamic_link_methodes(self):
        request = Obj()
        request.__dict__['META']={}
        request.META['HTTP_HOST']='www.testrunner.eu'
        link = '%s/%s/%s/%s/%s' % ('http://www.testrunner.eu',
                                'lg',
                                'serve/link',
                                self.dlink.get_link_key(),
                                self.file,
                                )
        self.assertEqual(link, self.dlink.get_link_url(request))
        