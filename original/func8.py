import json
import time
from typing import Dict

from original.encryption import encryption1
from extend import session, LG_DV_ARG
from util import jquery_random_call_back, pack_callback, replace_text2dict

_rzData = {
    "cl": [
        {
            "x": 241,
            "y": 422,
            "t": 1680698256160
        }
    ],
    "mv": [
        {
            "fx": 239,
            "fy": 23,
            "t": 1680698254044,
            "bf": 2
        },
        {
            "fx": 238,
            "fy": 26,
            "t": 1680698254249,
            "bf": 2
        },
        {
            "fx": 233,
            "fy": 196,
            "t": 1680698254434,
            "bf": 2
        },
        {
            "fx": 236,
            "fy": 273,
            "t": 1680698254614,
            "bf": 2
        },
        {
            "fx": 244,
            "fy": 447,
            "t": 1680698254802,
            "bf": 2
        },
        {
            "fx": 248,
            "fy": 516,
            "t": 1680698254989,
            "bf": 2
        },
        {
            "fx": 248,
            "fy": 515,
            "t": 1680698255214,
            "bf": 2
        },
        {
            "fx": 257,
            "fy": 385,
            "t": 1680698255431,
            "bf": 2
        },
        {
            "fx": 257,
            "fy": 376,
            "t": 1680698255664,
            "bf": 2
        },
        {
            "fx": 242,
            "fy": 418,
            "t": 1680698255844,
            "bf": 2
        }
    ],
    "sc": [],
    "kb": [],
    "sb": [],
    "sd": [],
    "sm": [],
    "cr": {
        "screenTop": 0,
        "screenLeft": 0,
        "clientWidth": 363,
        "clientHeight": 674,
        "screenWidth": 1366,
        "screenHeight": 768,
        "availWidth": 1366,
        "availHeight": 768,
        "outerWidth": 1366,
        "outerHeight": 768,
        "scrollWidth": 1203,
        "scrollHeight": 1203
    },
    "simu": 0,
    "ac_c": 0
}

_store = {
    "storeVer": "1.0.1",
    "count": 11,
    "countnum": 20,
    "nameL": "57a4c3ff",
    "nameR": "appsapi0",
    "sendUrl": "https://passport.baidu.com/viewlog",
    "hideHelp": False,
    "ExteriorSwitch": False,
    "styAnimaBtn": True,
    "doubleSucTac": True,
    "backupFeedUrl": "https://zhiqiu.baidu.com/imcswebchat/roulette/in?id=48907&token=m75585l8ssgl520b862a2588nm1j91oc&domainID=pass&type=2",
    "doubleSucFeedUrl": "",
    "slideTitle": None,
    "spinTitle": {},
    "senceTitleConfig": {
        "animaTipSence": {
            "slide": "请完成下方验证后继续操作",
            "spin": "请完成下方验证后继续操作"
        },
        "doubleSucSence": {
            "slide": "存在安全风险，请再次验证",
            "spin": "存在安全风险，请再次验证"
        }
    },
    "openYmg": False,
    "scene": "",
    "getStyleUrl": "https://passport.baidu.com/viewlog/getstyle",
    "qrstatus": "https://passport.baidu.com/viewlog/qrstatus",
    "ak": "1e3f2dd1c81f2075171a547893391274",
    "type": "default",
    "id": "mkd"
}

_dsData = {
    "ds": "",
    "tk": ""

}

_conf = {
    "maskModule": True,
    "ak": "1e3f2dd1c81f2075171a547893391274",
    "backstr": "3223-DMHEPLEVCjDdW3ZD5blTxoviGFTxaiA5vBsDBiqdO+twvGEQnYjZFU50wuXY72heXFApDG1xMM/efmjfe/cbx2DanhBkao/6gPY7IP0AjedgcT778D+L6NjqJGnm3xin9WEBD/6M8llFoOeKPD24cqFwO/Qr0Wikh7PBIP9u5vX2z+UEL88Caw9XbkZDfy/F9a20qSjbo5XhGYRlhRWNghpfkUB62IC4uxT9+blVg0qel1PEsgRB0iUnpvcP1hxsyW1rMJtnr29u2YN+8bWwrXgX9x7dnhIdlt2+ThjJ9l6ebvuCfXxj5SxmENXzdJUGI/2F767ZPB9clN85wIvL9A==",
    "type": "spin",
    "ext": {
        "img": "https%3A%2F%2Fpassport.baidu.com%2Fviewlog%2Fimg%3Fid%3D3223-DMHEPLEVCjDdW3ZD5blTxoviGFTxaiA5vBsDBiqdO%252BtwvGEQnYjZFU50wuXY72heXFApDG1xMM%252Fefmjfe%252Fcbx2DanhBkao%252F6gPY7IP0AjedgcT778D%252BL6NjqJGnm3xin9WEBD%252F6M8llFoOeKPD24cqFwO%252FQr0Wikh7PBIP9u5vX2z%252BUEL88Caw9XbkZDfy%252FF9a20qSjbo5XhGYRlhRWNghpfkUB62IC4uxT9%252BblVg0qel1PEsgRB0iUnpvcP1hxsyW1rMJtnr29u2YN%252B8bWwrXgX9x7dnhIdlt2%252BThjJ9l6ebvuCfXxj5SxmENXzdJUGI%252F2F767ZPB9clN85wIvL9A%253D%253D%26ak%3D1e3f2dd1c81f2075171a547893391274%26tk%3D616047oxsNNNvCOWdHOC742KdxN31sMWX5ucLZ7XV5GBcWzth9XowKy0lbohhgOduOE116VdEbrRff%252BPgfC%252BK3cFSifB%252F0leUhe3PYFCjGlKrHzyIJFnAvyapJHtq7hgQBvr",
        "info": "摄影师：du小炮兵 该作品经[baidu]版权存证",
        "sup": 1
    }
}


def login_fn(e: Dict, t: Dict, n: Dict):
    n["timeSpan"] = int(time.time() * 1000) - e.get("initTime")
    n["countrycode"] = ""
    n["FP_UID"] = ""
    n["FP_INFO"] = ""
    n["loginVersion"] = "v4"
    n["supportdv"] = "1"
    n["bdint_sync_cookie"] = ""
    n["ds"] = t.get("ds", "")
    n["tk"] = t.get("tk", "")
    n["dv"] = LG_DV_ARG["dvjsInput"]
    n["fuid"] = "FOCoIC3q5fKa8fgJnwzbE67EJ49BGJeplOzf" \
                "+4l4EOvDuu2RXBRv6R3A1AZMa49I27C0gDDLrJyxcIIeAeEhD8JYsoLTpBiaCXhLqvzbzmvy3SeAW17tKgNq/Xx" \
                "+RgOdb8TWCFe62MVrDTY6lMf2GrfqL8c87KLF2qFER3obJGnjiLb/rMwxEvVVuyPNNNl4GEimjy3MrXEpSuItnI4KD9MnM35" \
                "/VGxYufd0UYIwbu0cW75Db8WhomcJu" \
                "+x2nrVmXft9nx2n76hgVSijFwbwMBJsVwXkGdF24AsEQ3K5XBbh9EHAWDOg2T1ejpq0s2eFy9ar" \
                "/j566XqWDobGoNNfmfpaEhZpob9le2b5QIEdiQeMGGtnCq9fZ/aAmiQfaXFfXhLZ126CPFCIEuj/nWa+RPzg/CQV+t396RcQ" \
                "+QB5B6TasmgOrJ40n63OsKSOpoSLpklEtTKfx5hHc9j4nurRraXUHgNWSPA31ou" \
                "+XTSfsKyVXVSGGnkUB7qA0khSm2nsQwBpdgqbXUb4lU+zNAV2n0AktybhhKxhReRo8jZOXronbjpyaNZANNqEA4g1HmtdHmv" \
                "/tVUjVExnyBvjSrtrPu8IrnpcuigpPlr6uwWt" \
                "/lm7TLIKKJqASWGtMQ6010Ekmrx4fAQe4UGeL1qFLCkLufcHrqfCa5DTkTHzExvWtxZ2QvyTjxXMcJvDDEe3McIycHFbZmbEY9" \
                "LT3RuWsSjij5HIeKAxeCJRzKQmiJrt2NdSKvywx+j+Lr1+UH4yIiICKGteyr20MMrmevIGEgV8AB2DZ99xPOTpxsivktP0eWN/q" \
                "1uQn9VsBjBmLNQsYnwiX1i39zQE19TGybrzqrM1pMrcfAL1vAAGPaqoVSU+0UqC6Ax2W4+eWZGSFET4OOzFASXPux8VNAq3GJK6" \
                "GH5F7Bx8VJ2MfThAR9JY85BUmPjqOlbhrblXFkBQG7n4JKiZyalk9X22FXe2MsdipOHFxSUHSqbPo2PPJzEor12m6lThR7YgmlfL" \
                "t7kntJD5XeM7GEQw3OLo5dsSUeQDd6vDnkb72/TMYcbPW48WuSnSgMDL820G6v5sII3fbIl1IswRGEQw3OLo5dsSUeQDd6vDntVl" \
                "lC1+aCCc8K28RWpYmU0S24R9DDZVx3j3+tLLpw3BRuF/lI7yGQ5dEntCEMtnVaOBuNLhAhlddA7KpjMdW1UU5ZZ2QvNYYVj4Mcvs" \
                "dmZl2ssb09Yk1KUaxhNd9iuw6w== "





def mkd_data_login_fn(e: Dict, i: Dict):
    """
    e.mkdDataLoginFn = function() {
        if (e.loginPassMkd && e.loginPassMkd.getDataAsync) {
            e.currentPath = "mkdDataLoginFn";
            var t = {};
            e.loginPassMkd.getDataAsync(function(n) {
                t.ds = n.ds || "xxx_loginv4",
                t.tk = n.tk || "xxx_loginv4",
                e.loginFn(t, i)
            })
        } else
            e.loginFn(null, i)
    }
    """
    e["currentPath"] = "mkdDataLoginFn"
    get_data_async(lambda n: login_fn(e, {
        "ds": n.get("ds", "xxx_loginv4"),
        "tk": n.get("tk", "xxx_loginv4")
    }, i))


def get_data_async(t):
    count = _store.get("count")
    if count > 0:
        poss_data(lambda e: callable(t) and t(e) if "data" in e else callable(t) and t(_dsData), None)
    else:
        callable(t) and t(_dsData)


def poss_data(t, i):
    def _func_o(e, v_t):
        """
        function(t, i) {
            var r = e.PassMachine.haveMkd || this
              , o = function(e, t) {
                if (1 === b)
                    return r.removeGatherEvent && r.removeGatherEvent(),
                    r.removeVcodeEvent && r.removeVcodeEvent(),
                    !1;
                var i = JSON.stringify(r.rzData)
                  , o = r.encrypt(i)
                  , s = {};
                s.ak = r.store.ak,
                s.as = r.store.nameL || "",
                s.fs = o,
                s.tk = r.dsData.tk || "",
                s.scene = r.conf.scene || "",
                t && (s.cv = t),
                r.store.count = 0,
                r.initMock(),
                n.ajax({
                    url: r.store.sendUrl,
                    dataType: "jsonp",
                    data: s,
                    time: 18e4,
                    success: function(t) {
                        if (0 === t.code && t.data) {
                            r.dsData = t.data || {},
                            r.store.nameL = t.data.as || "6bffae1c";
                            var n = t.data;
                            delete n.as,
                            e && e(n)
                        } else
                            1 === t.code ? (r.removeGatherEvent && r.removeGatherEvent(),
                            r.removeVcodeEvent && r.removeVcodeEvent(),
                            b = 1) : (r.errorData(),
                            e && e(r.dsData))
                    },
                    error: function() {
                        r.errorData(),
                        e && e(r.dsData)
                    }
                })
            };
            r.store.openYmg ? r.getYmgData(function() {
                o(t, i)
            }) : o(t, i)
        },
        """
        i = json.dumps(_rzData)
        o = encryption1(i, _store.get("nameL", "") + _store.get("nameR", ""))
        s = {
            "ak": _store.get("ak", ""),
            "as": _store.get("nameL", ""),
            "fs": o,
            "tk": _dsData.get("tk", ""),
            "scene": _conf.get("scene", "")
        }
        if t:
            s["cv"] = t
        _store["count"] = 0
        _init_mock()
        s["callback"] = jquery_random_call_back()
        s["_"] = int(time.time() * 1000)
        response = session.get(url=_store.get("sendUrl"), params=s)
        response_dict = replace_text2dict(response.text, s.get("callback"))
        _dsData["ds"] = response_dict.get("ds", "")
        _dsData["as"] = response_dict.get("as", "")
        _dsData["tk"] = response_dict.get("tk", "")
        _store["nameL"] = response_dict.get("as", "6bffae1c")
        response_dict.pop("as", "")
        if t and callable(t):
            t(response_dict)

    # open_ymg = _store.get("openYmg", None)
    # if open_ymg:

    _func_o(t, i)


def _init_mock():
    """
    function() {
        this.rzData = {
            cl: [],
            mv: [],
            sc: [],
            kb: [],
            sb: [],
            sd: [],
            sm: [],
            cr: s(),
            simu: window.navigator.webdriver ? 1 : 0,
            ac_c: 0
        },
        this.dsData = {}
    },
    """
    _rzData["cl"] = []
    _rzData["mv"] = []
    _rzData["sc"] = []
    _rzData["kb"] = []
    _rzData["sb"] = []
    _rzData["sd"] = []
    _rzData["sm"] = []
    _rzData["simu"] = 0
    _rzData["ac_c"] = 0
    _dsData["ds"] = ""
    _dsData["tk"] = ""
