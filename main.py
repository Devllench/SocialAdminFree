#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import wsgiref.handlers
import wsgiref
from wsgiref import util


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])

    #response_body = util.FileWrapper(open('home.html'))
    response_body = 'Hello'
    return [response_body.encode()]


wsgiref.handlers.CGIHandler().run(application)


