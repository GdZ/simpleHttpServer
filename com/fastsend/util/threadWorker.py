# -*- coding: utf-8 -*-
"""
Worker used by ThreadPool class.
"""
__author__ = 'MR.Z'

from threading import Thread

class Worker(Thread):
    """Thread executing tasks from a given tasks queue"""
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()

            try:
                func(*args, **kargs)
            except Exception, e:
                print e

            self.tasks.task_done()
