# @Time    : 2023/04/06 10:54
# @Author  : fyq
# @File    : extend.py
# @Software: PyCharm

__author__ = 'fyq'

import time

import requests

from original.func9 import S
from util import create_page_token

_headers = {
    "Host": "passport.baidu.com",
    "Referer": "https://zhidao.baidu.com/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/111.0.0.0 Safari/537.36 "
}

session = requests.session()
session.headers = _headers

b = {
    "tpl": "pp",
    "SendMethod": 9,
    "ExcludeTarget": [
        "password"
    ],
    "Token": create_page_token(),
    "RCMSEvent": 5,
    "RCKSEvent": 5,
    "RCMVEvent": 5,
    "RCTVEvent": 5,
    "RCFCEvent": 5,
    "ImgUrl": "//baidu.com/error.jsonp?n=",
    "Flag": 16777215
}

F = {
    "EnableKSEvent": b.get("Flag") >> 1 & 1,
    "EnableMCEvent": b.get("Flag") >> 2 & 1,
    "EnableMPEvent": b.get("Flag") >> 3 & 1,
    "RecordTimeInterval": b.get("Flag") >> 6 & 1,
    "BrowserInfo": True,
    "LSIDInfo": True,
    "Location": True,
    "Token": b.get("Flag") >> 12 & 1,
    "ScreenInfo": True,
    "FlashInfo": True,
    "DVID": b.get("Flag") >> 17 & 1,
    "PageToken": b.get("Token"),
    "ImgUrl": b.get("ImgUrl"),
    "EltAttrs": [],
    "RCInterval": 50,
    "RCMSEvent": b.get("RCMSEvent", 5),
    "RCKSEvent": b.get("RCKSEvent", 5),
    "RCMVEvent": b.get("RCMVEvent", 5),
    "RCFCEvent": b.get("RCFCEvent", 0),
    "SendInterval": 1,
    "SendMethod": b.get("SendMethod", 0),
    "GYInterval": b.get("GYInterval", 50),
    "RCGPEvent": b.get("RCGPEvent", 5),
    "RCTVEvent": b.get("RCTVEvent", 5),
    "DVHost": b.get("DVHost", "passport.baidu.com"),
    "SendTimer": b.get("SendTimer", 1e3),
}

LG_DV_ARG = {

}


def I():
    w = {
        "mouseDown": "",
        "keyDown": "",
        "mouseMove": "",
        "version": 26,
        "loadTime": int(time.time() * 1000) / 1000,
        "browserInfo": "1,2,101",
        "token": F.get("PageToken"),
        "location": "https://zhidao.baidu.com/,undefined",
        "screenInfo": "0,0,205,2102,1920,1080,1920,1920,1040",
        "flashInfo": None
    }

    LG_DV_ARG["dvjsInput"] = w.get("token") + "@" + S(w, w.get("token"))


F["SendMethod"] = F["SendMethod"] | 1

I()

