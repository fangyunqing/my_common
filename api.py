# @Time    : 2023/03/21 11:54
# @Author  : fyq
# @File    : info.py
# @Software: PyCharm

__author__ = 'fyq'

import uuid
import original.func2 as o_func2
import original.func3 as o_func3


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

    e = "getApiInfo"
    p = {
        "fillUserName": {
            "selectedSuggestName": "pass_fillinusername_suggestuserradio",
            "timeSpan": "ppui_fillusernametime"
        },
        "getApiInfo": {
            "apiType": "class",
        },
        "login": {
            "isPhone": "isPhone",
            "logLoginType": "logLoginType",
            "memberPass": "mem_pass",
            "safeFlag": "safeflg",
            "timeSpan": "ppui_logintime"
        },
        "reg": {
            "logRegType": "logRegType",
            "password": "loginpass",
            "selectedSuggestName": "pass_reg_suggestuserradio_0",
            "suggestIndex": "suggestIndex",
            "suggestType": "suggestType",
            "timeSpan": "ppui_regtime"
        },
        "regPhone": {
            "logRegType": "logRegType",
            "password": "loginpass",
            "selectedSuggestName": "pass_reg_suggestuserradio_0",
            "suggestIndex": "suggestIndex",
            "suggestType": "suggestType",
            "timeSpan": "ppui_regtime"
        }
    }

    m = {
        "login": {
            "memberPass": lambda v_e: "on" if v_e else ""
        },
        "loginCheck": {
            "isPhone": lambda v_e: "true" if v_e else "false"
        }
    }

    i = o_func2.i(n, e, p.get(e, None), m.get(e, None), False)
    d = "https://passport.baidu.com"
    t = "/v2/api/?getapi"
    s = {
        "charset": "utf-8",
        "processData": ""
    }

    return o_func3.jsonp(d + t, i, s) + "&callback=bd__cbs__mzuv9b"


