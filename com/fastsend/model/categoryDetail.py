# -*- coding: utf-8 -*-
import logging
__author__ = 'self'

Log = logging.getLogger('fastsend.server')

def getCategoryDetail():
    Log.info('gdz.log getCategoryDetail')
    imgList = []
    for i in range(0, 4, 1):
        img = {}
        img['url'] = 'http://xxoo/' + str(i) + '.jpg'
        img['to'] = 'activityDetail'
        img['title'] = '图标说明-' + str(i)
        imgList.append(img)
    itemList = []
    for j in range(0, 6, 1):
        item = {}
        item['index'] = j
        item['List'] = imgList
        itemList.append(item)
    return itemList