# -*- coding: utf-8 -*-
import logging
import simplejson as json

from com.fastsend.const.statics import CONST_MODEL_HOME_TYPE_AD
from com.fastsend.const.statics import CONST_MODEL_HOME_TYPE_API
from com.fastsend.const.statics import CONST_MODEL_HOME_TYPE_RICE
from com.fastsend.const.statics import CONST_ITEM_TITLE_STR

__author__ = 'self'

Log = logging.getLogger('fastsend.server')

def getHomeContent():
    hc = {}
    hc['data'] = getData()
    return hc

def getData():
    Log.info('gdz.log getData --begin')
    dataList = []
    dataList.append(getContent(CONST_MODEL_HOME_TYPE_AD))
    dataList.append(getContent(CONST_MODEL_HOME_TYPE_API))
    dataList.append(getContent(CONST_MODEL_HOME_TYPE_RICE))
    Log.info('gdz.log getData --end')
    return dataList

def getContent(type):
    Log.info('gdz.log getContent --begin')
    details = []
    for i in range(0, 2, 1):
        img = {}
        if type == CONST_MODEL_HOME_TYPE_AD:
            img['id'] = i
            img['imgUrl'] = "http://img30.360buyimg.com/mobilecms/jfs/t2068/42/1458838150/43274/b628ca03/5656baedN26b1d066.jpg"
        elif type == CONST_MODEL_HOME_TYPE_API:
            img['id'] = i
            img['iconUrl'] = "http://img30.360buyimg.com/mobilecms/jfs/t2575/168/230804041/5320/a0f524bf/5651cdc7N2737a3a4.png"
            img['title'] = "超市生鲜-" + str(i)
        elif type == CONST_MODEL_HOME_TYPE_RICE:
            img['proId'] = str(200 + i)
            img['proDes'] = "商品描述-" + str(i)
            img['proImgUrl'] = "http://img30.360buyimg.com/mobilecms/jfs/t2005/32/888677243/67965/d8bffaf1/5632cfabN2202ccb3.jpg"
            img['proPrice'] = str(50 + i*3)
        details.append(img)

    item = {}
    item['index'] = 0
    if type == CONST_MODEL_HOME_TYPE_AD:
        item['itemTitle'] = CONST_ITEM_TITLE_STR['ad']
    elif type == CONST_MODEL_HOME_TYPE_API:
        item['itemTitle'] = CONST_ITEM_TITLE_STR['type_api']
    elif type == CONST_MODEL_HOME_TYPE_RICE:
        item['itemTitle'] = CONST_ITEM_TITLE_STR['rice_oil']
    item['itemType'] = 'ids'
    item['itemCode'] = '0'
    item['itemPos'] = 'postion'
    item['timer'] = 1448358504000
    item['data'] = details
    Log.info('gdz.log getContent --end')
    return item
