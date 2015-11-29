# -*- coding: utf-8 -*-
import logging
__author__ = 'self'

Log = logging.getLogger('fastsend.server')

def getHomeContent():
    Log.info('gdz.log getHomeContent')
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
        item['itemTitle'] = '广告'
        item['itemType'] = 'ids'
        item['itemCode'] = '0'
        item['itemPos'] = 'postion'
        item['timer'] = 1448358504000
        item['List'] = imgList
        itemList.append(item)
    return itemList