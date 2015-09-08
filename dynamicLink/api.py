#!/usr/bin/python
# -*- coding:utf-8 -*-
# This Python file uses the following encoding: utf-8

from models import Download
import presettings


def file_link_url(request, linkobject, langcode='lg'):
    """returns the access url of the of the dynamicLink object"""
    return '%s%s/%s/%s/link/%s/%s' % ('http://', request.META.get('HTTP_HOST'), \
            langcode, presettings.DYNAMIC_LINK_URL_BASE_COMPONENT, linkobject.link_key, \
            linkobject.get_filename())

class DynamicLink:
    """
    create and access dynamic links form outsite of this app
    """
    def __init__(self, slug, file_path, timeout_hours=None, max_clicks=None):
        """creates a new dynamic link"""
        self.new_link = Download()
        self.new_link.slug = slug
        self.new_link.file_path = file_path

        if timeout_hours:
            self.new_link.timeout_hours = timeout_hours
        if max_clicks:
            self.new_link.max_clicks = max_clicks

        self.new_link.save()

    def get_link_key(self):
        """get his unique key"""
        return self.new_link.link_key

    def get_link_url(self, request, langcode='lg'):
        """access his url"""
        return file_link_url(request, self.new_link, langcode)

class DownloadSiteUrl():
    """
    create a download site with links from the given keys
    """
    def __init__(self, keylist=None):
        """you can add a list with keys"""
        self.keys = []
        if keylist:
            self.keys += keylist

    def add_key(self,key):
        """add a key to allready given keys"""
        self.keys.append(key)

    def get_site_url(self, request, langcode='lg'):
        """returns a site urls form allready given keys"""
        return '%s%s/%s/%s/site/%s' % ('http://', request.META.get('HTTP_HOST'), \
        langcode, presettings.DYNAMIC_LINK_URL_BASE_COMPONENT, '-'.join(self.keys))








