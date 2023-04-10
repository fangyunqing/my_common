# @Time    : 2023/03/21 11:54
# @Author  : fyq
# @File    : info.py
# @Software: PyCharm

__author__ = 'fyq'

import json
import time
from typing import Dict

from requests import Session

import original.func2 as o_func2
import original.func3 as o_func3
from encryption.rsa import rsa
from extend import g_p, g_m
from original.func8 import mkd_data_login_fn
from util import _guid_random, random_callback, pack_callback


def get_api_info(session: Session):
    n = {
        "apiType": "login",
        "gid": _guid_random(),
        "loginType": "dialogLogin",
        "loginVersion": "v4",
    }

    e = "getApiInfo"
    i = o_func2.i(n, e, g_p.get(e, None), g_m.get(e, None), False)
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
    e = {"initTime": int(time.time() * 1000)}
    mkd_data_login_fn(e, i)


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



