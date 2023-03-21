# @Time    : 2023/03/21 12:52
# @Author  : fyq
# @File    : func2.py
# @Software: PyCharm

__author__ = 'fyq'

import datetime
import time
from urllib.parse import unquote

_ = {
    "charset": "GBK",
    "product": "ik",
    "staticPage": "https://zhidao.baidu.com/static/common/https-html/v3Jump.html",
    "subpro": "",
    "token": ""
}

_f = {
    "checkPassword": {
        "fromreg": 1
    },
    "reg": {
        "registerType": 1,
        "verifypass": lambda e: e["password"] if "password" in e else None
    }
}

_h = {
    "password": True
}


def i(e, t, n, r, s: bool):
    if s:
        o = {
            "staticpage": _["staticPage"],
            "charset": _["charset"]
        }
    else:
        o = {}

    if t in _f:
        for t_key, t_val in _f[t].items():
            if callable(t_val):
                o[t_key] = t_val(e)
                if t_key == "verifypass":
                    o[t_key] = unquote(o[t_key])

    o["token"] = _["token"]
    o["tpl"] = _["product"]
    o["subpro"] = _["subpro"]
    o["apiver"] = "v3"
    o["tt"] = int(time.time() * 1000)
    if e:
        n = n if n else {}
        r = r if r else {}
        for e_key, e_val in e:
            if e_key in r:
                u = r[r](e_val, e)
            else:
                u = e_val
            if isinstance(u, str):
                if s:
                    u = unquote(u)
                if e_key not in _h or not _h[e_key]:
                    u = u.strip()


