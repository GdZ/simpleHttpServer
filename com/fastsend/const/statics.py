# -*- coding: utf-8 -*-
__author__ = 'self'

# hier ist fuer const global variables {
CONST_MODEL_HOME_TYPE_AD = 0
CONST_MODEL_HOME_TYPE_API = 1
CONST_MODEL_HOME_TYPE_RICE = 2

CONST_ITEM_TITLE_STR = {
    'ad' : "广告",
    'type_api' : "分类入口",
    'rice_oil':"粮油米面"
}
# } gdz.commit end

# api configs {
API_BASE = "/api"
API_VER = "/v0.1"
API_ROOT = API_BASE + API_VER # /api/v0.1

API_HOME_BASE = "/home"
API_HOME = API_ROOT + API_HOME_BASE

API_CATEGORY_LIST_BASE = "/categoryList"
API_CATEGORY_LIST = API_ROOT + API_CATEGORY_LIST_BASE

API_CATEGORY_DETAIL_BASE = "/categoryDetail"
API_CATEGORY_DETAIL = API_ROOT + API_CATEGORY_LIST_BASE
# } gdz.commit end
