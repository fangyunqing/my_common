# @Time    : 2023/03/21 12:52
# @Author  : fyq
# @File    : func2.py
# @Software: PyCharm

__author__ = 'fyq'

import time
from typing import Any, Dict
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


def i(e: Dict[str, Any], t, n, r, s: bool):
    """
        function i(e, t, n, i, s) {
            var o = s ? {
                staticpage: _.staticPage,
                charset: _.charset || document.characterSet || document.charset || ""
            } : {}
              , a = f[t];
            if (a)
                for (var r in a) {
                    if (a.hasOwnProperty(r)) {
                        var l = a[r];
                        o[r] = "function" == typeof l ? l(e) : l
                    }
                    "verifypass" == r && (o[r] = decodeURIComponent(o[r]))
                }
            if (o.token = _.token || "",
            o.tpl = _.product || "",
            o.subpro = _.subpro || "",
            o.apiver = "v3",
            o.tt = (new Date).getTime(),
            e) {
                n = n || {},
                i = i || {};
                for (var r in e)
                    if (e.hasOwnProperty(r)) {
                        var d = i[r]
                          , u = d ? d(e[r], e) : e[r];
                        "string" == typeof u && (s && (u = decodeURIComponent(u)),
                        h[r] || (u = c.trim(u))),
                        o[n[r] || r.toLowerCase()] = u
                    }
            }
            return o
        }
    """
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
        for e_key, e_val in e.items():
            if e_key in r:
                u = r[e_key](e_val)
            else:
                u = e_val
            if isinstance(u, str) and s:
                u = unquote(u)
            if e_key in n:
                o[n[e_key]] = u
            else:
                o[e_key.lower()] = u

    return o
