# @Time    : 2023/03/22 9:22
# @Author  : fyq
# @File    : func4.py
# @Software: PyCharm

__author__ = 'fyq'

import time

n = "moonshad5moonsh2"
i = "moonshad3moonsh0"
o = "moonshad8moonsh6"
a = "moonshad0moonsh1"
s = "moonshad1moonsh9"
h = {
    "version": "v3"
}


def c(t, r, e):
    """
        function c(t, r, e) {
            if (!window.screen.width || !window.screen.height)
                return {};
            var n = {};
            try {
                var i = f(t || {});
                i.alg = h.version,
                i.time = Math.round((new Date).getTime() / 1e3),
                i.hasOwnProperty("sig") && delete i.sig,
                i.hasOwnProperty("traceid") && delete i.traceid,
                i.hasOwnProperty("callback") && delete i.callback,
                i.hasOwnProperty("elapsed") && delete i.elapsed,
                i.hasOwnProperty("shaOne") && delete i.shaOne;
                var o, a = "";
                for (o = a = (new Date).getTime(); "00" !== (a = l(d(a))).toString().substr(0, 2); )
                    ;
                if (n = {
                    time: i.time,
                    alg: i.alg,
                    sig: h.encryption(i, r, e),
                    elapsed: (new Date).getTime() - o || "",
                    shaOne: a
                },
                window.passFingerPrint) {
                    var s = window.passFingerPrint();
                    n.rinfo = p({
                        fuid: d(s.fuid)
                    })
                }
            } catch (c) {
                u(c)
            }
            return n
        }
    """
    v_i = {k: v for k, v in t.items()}
    v_i["alg"] = h["version"]
    v_i["time"] = round(time.time())
    v_i.pop("sig", "")
    v_i.pop("traceid", "")
    v_i.pop("callback", "")
    v_i.pop("elapsed", "")
    v_i.pop("shaOne", "")
    v_o = None
    v_a = None
    while True:
        v_a = int(time.time() * 1000)
        v_o = v_a


