#############################################
# -*- coding: utf-8 -*-
# simpleHttpServer request handler.
# @2015.11.29 by zgd_521@yahoo.com
#############################################
__author__ = 'MR.Z'

import logging
import socket
import simplejson as json
from com.fastsend.sys.fileHelper import get_file
from com.fastsend.net.httpRequest import parse_http_request
from com.fastsend.net.httpResponse import HttpResponse
from com.fastsend.util.threadPool import ThreadPool
from com.fastsend.model.home import getHomeContent
from com.fastsend.model.categoryList import getCategoryList
from com.fastsend.model.categoryDetail import getCategoryDetail
from com.fastsend.config.cfg import RECV_BUFSIZ
from com.fastsend.config.cfg import THREAD_POOL_SIZE
from com.fastsend.config.cfg import SOCKET_BACKLOG_SIZE

Log = logging.getLogger('fastsend.server')

def handle_request(clientsock):

    data = clientsock.recv(RECV_BUFSIZ)

    Log.debug('Request received:\n%s', data)

    request = parse_http_request(data)
    Log.debug('gdz.log request.request_uri ist: %s', request.request_uri)

    params = {}
    i = 0
    for item in str(request.request_uri[1:]).split('/'):
        key, value = i, item
        params[key] = value
        i = i+1
    Log.debug('gdz.log params: %s', json.dumps(params))
    file = get_file(params[2])
    Log.debug('gdz.log file.info: %s', json.dumps(file.__dict__))

    result = {}
    if params[0] == 'api':
        Log.debug('gdz.log 0. heute ist api')
        response = HttpResponse(protocol=request.protocol, status_code=200)
        response.headers['charset'] = 'utf-8'
        response.headers['Content-type'] = 'text/plain'
        result['code'] = 0
        result['msg'] = '请求主页成功'
        result['success'] = 'true'
        if params[2] == 'home':
            result['result'] = getHomeContent()
        elif params[2] == 'categoryList':
            result['result'] = getCategoryList()
        elif params[2] == 'categoryDetail':
            result['result'] = getCategoryDetail()
        Log.info(json.dumps(result))
        response.content = json.dumps(result)
    elif file.exists and request.is_range_requested():
        Log.debug('gdz.log 1. ist range requested.')
        response = HttpResponse(protocol=request.protocol, status_code=206,
                                range=request.get_range())
        response.file = file

    elif file.exists:
        Log.debug('gdz.log 2. file exists.')
        response = HttpResponse(protocol=request.protocol, status_code=200)
        response.headers['charset'] = 'utf-8'
        response.file = file

    else:
        Log.debug('gdz.log 3. file ist not gefunden.')
        response = HttpResponse(protocol=request.protocol, status_code=404)
        response.headers['Content-type'] = 'text/plain'
        response.headers['charset'] = 'utf-8'
        response.content = 'This file does not exist!'

    Log.info('GET %s %s %s %s',
             request.request_uri, request.protocol, request.get_range(), response.status_code)

    response.write_to(clientsock)
    clientsock.close()

def run(host, port):
    address = (host, port)
    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversock.bind(address)
    serversock.listen(SOCKET_BACKLOG_SIZE)

    Log.info('fastsend started on %s:%s' % (host, port, ))

    pool = ThreadPool(THREAD_POOL_SIZE)

    while True:
        Log.debug('Waiting for connection...')

        clientsock, addr = serversock.accept()
        Log.debug('Connected from: %s', addr)

        pool.add_task(handle_request, clientsock)

