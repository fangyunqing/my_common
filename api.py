# @Time    : 2023/03/21 11:54
# @Author  : fyq
# @File    : info.py
# @Software: PyCharm

__author__ = 'fyq'

import json
import random
import string
import uuid
from typing import Dict

from requests import Session

import original.func2 as o_func2
import original.func3 as o_func3
from encryption.rsa import rsa


def _guid_random():
    guid = str(uuid.uuid4()).upper()
    return guid[1: len(guid)] + guid[0]


def random_callback(rule="??__???__??????"):
    res = ""
    for index, r in enumerate(rule):
        if r == "?":
            if index in [0, 1] or random.randint(0, 1) == 0:
                res += random.choice(string.ascii_lowercase)
            else:
                res += str(int(random.random() * 10))
        else:
            res += r
    return res


def pack_callback(call_back):
    return "&call_back=" + call_back


def get_api_info(session: Session):
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

    url = o_func3.jsonp(d + t, i, s)
    call_back = random_callback()
    response = session.get(url=url + pack_callback(call_back))
    response_dict: Dict = json.loads(
        response.text.replace(call_back, "").replace(")", "").replace("(", "").replace("'", '"'))
    return {
        "token": response_dict.setdefault("data").get("token", None)
    }


def login(session: Session, **kwargs):
    password = kwargs.get("password", "")
    username = kwargs.get("username", "")
    token = kwargs.get("token", "")
    public_key = kwargs.get("pubkey", "")
    key = kwargs.get("key", "")
    i = {
        "codeString": "",
        "detect": "1",
        "gid": _guid_random(),
        "idc": "",
        "isPhone": "",
        "logLoginType": "pc_loginDialog",
        "loginMerge": "true",
        "logintype": "dialogLogin",
        "memberPass": "on",
        "mkey": "",
        "password": rsa(public_key, password),
        "quick_user": "0",
        "safeFlag": "0",
        "splogin": "rate",
        "staticPage": "https://zhidao.baidu.com/static/common/https-html/v3Jump.html",
        "subpro": "",
        "u": "https://zhidao.baidu.com/",
        "userName": username,
        "verifyCode": "",
        "token": token,
        "rsaKey": key,
        "crypttype": 12,
    }





def get_public_key(session: Session):
    n = {
        "gid": _guid_random(),
        "loginVersion": "v5",
    }

    d = "https://passport.baidu.com"
    t = "/v2/getpublickey"
    e = "getRsaKey"
    s = {
        "charset": "utf-8",
        "processData": ""
    }

    i = o_func2.i(n, e, None, None, False)
    url = o_func3.jsonp(d + t, i, s)
    call_back = random_callback()
    response = session.get(url=url + pack_callback(call_back))
    response_dict: Dict = json.loads(
        response.text.replace(call_back, "").replace(")", "").replace("(", "").replace("'", '"'))
    return {
        "pubkey": response_dict.get("pubkey", None),
        "key": response_dict.get("key", None),
    }
