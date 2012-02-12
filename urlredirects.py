#!/usr/bin/env python 
import urllib2
from collections import namedtuple

URLRedirect = namedtuple('URLRedirect', 'urlhandle, redirects')

class SmartRedirectHandler(urllib2.HTTPRedirectHandler):     
    def __init__(self):
        self.redirect_list = list()

    def http_error_301(self, req, fp, code, msg, headers):  
        if 'location' in headers:
            self.redirect_list.append((code,\
                headers.getheaders('location')[0]))
        elif 'uri' in headers:
            self.redirect_list.append((code,\
                headers.getheaders('uri')[0]))
        result = urllib2.HTTPRedirectHandler.http_error_301( 
            self, req, fp, code, msg, headers)              
        result.status = code                                
        return result                                       

    def http_error_302(self, req, fp, code, msg, headers):   
        if 'location' in headers:
            self.redirect_list.append((code,\
                headers.getheaders('location')[0]))
        elif 'uri' in headers:
            self.redirect_list.append((code,\
                headers.getheaders('uri')[0]))
        result = urllib2.HTTPRedirectHandler.http_error_302(
            self, req, fp, code, msg, headers)              
        result.status = code                                
        return result
    def http_error_303(self, req, fp, code, msg, headers):   
        if 'location' in headers:
            self.redirect_list.append((code,\
                headers.getheaders('location')[0]))
        elif 'uri' in headers:
            self.redirect_list.append((code,\
                headers.getheaders('uri')[0]))
        result = urllib2.HTTPRedirectHandler.http_error_303(
            self, req, fp, code, msg, headers)              
        result.status = code                                
        return result

    def http_error_307(self, req, fp, code, msg, headers):   
        if 'location' in headers:
            self.redirect_list.append((code,\
                headers.getheaders('location')[0]))
        elif 'uri' in headers:
            self.redirect_list.append((code,\
                headers.getheaders('uri')[0]))
        result = urllib2.HTTPRedirectHandler.http_error_303(
            self, req, fp, code, msg, headers)              
        result.status = code                                
        return result

def get_redirects(url):
    request = urllib2.Request(url)
    # httplib.HTTPConnection.debuglevel = 1
    handler = SmartRedirectHandler()
    opener = urllib2.build_opener(handler)
    f = opener.open(request)
    return URLRedirect(f, handler.redirect_list)
