# -*- coding: utf-8 -*-
"""
simpleHttpServer runner.
"""
import logging
from com.fastsend.main.deamon import doTask
from com.fastsend.config.cfg import HOST
from com.fastsend.config.cfg import PORT
from com.fastsend.config.cfg import setup_logging

Log = logging.getLogger('simpleHttpServer.run')

if __name__ == '__main__':
    setup_logging()

    try:
        doTask(h=HOST, p=PORT)
    except KeyboardInterrupt:
        Log.info('simpleHttpServer stopped')
