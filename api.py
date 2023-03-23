# @Time    : 2023/03/21 11:54
# @Author  : fyq
# @File    : info.py
# @Software: PyCharm

__author__ = 'fyq'

import uuid

d = "https://passport.baidu.com"
t = "/v2/api/?getapi"


def _guid_random():
    guid = str(uuid.uuid4()).upper()
    return guid[1: len(guid)] + guid[0]


def get_api_info():
    n = {
        "apiType": "login",
        "gid": _guid_random(),
        "loginType": "dialogLogin",
        "loginVersion": "v4",
    }
