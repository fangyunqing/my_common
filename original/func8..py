from typing import Dict

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


def login_connect(e: Dict, t, n):
    """
    loginConnect: function(e, t, n) {
        ({
            username: e.username,
            smsVcode: e.smsVcode || "",
            sms: e.sms || ""
        }),
        n()
    }
    """
    data = {
        "username": e.get("username", ""),
        "smsVcode": e.get("smsVcode", ""),
        "sms": e.get("sms", "")
    }


def mkd_data_login_fn():
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


def get_data_async():
    pass


def poss_data():
    pass