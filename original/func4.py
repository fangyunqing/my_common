# @Time    : 2023/03/22 9:22
# @Author  : fyq
# @File    : func4.py
# @Software: PyCharm

__author__ = 'fyq'

import time
import original.func5 as o_func5
import original.func1 as o_func1
from original.encryption import encryption

_n = "moonshad5moonsh2"
_i = "moonshad3moonsh0"
_o = "moonshad8moonsh6"
_a = "moonshad0moonsh1"
_s = "moonshad1moonsh9"
_h = {
    "version": "v3"
}

moonshadV3 = {
    "OOOO00": lambda t, r: c(t, r, _n),
    "OOO00O": lambda t, r: c(t, r, _i),
    "OOO000": lambda t, r: c(t, r, _o),
    "OOO0OO": lambda t, r: c(t, r, _a),
    "O0OOO0": lambda t, r: c(t, r, _s)
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
    v_i["alg"] = _h["version"]
    v_i["time"] = round(time.time())
    v_i.pop("sig", "")
    v_i.pop("traceid", "")
    v_i.pop("callback", "")
    v_i.pop("elapsed", "")
    v_i.pop("shaOne", "")
    v_o = int(time.time() * 1000)
    v_a = v_o
    while True:
        v_a = o_func5.i(o_func5.g(o_func5.o(o_func1.g(v_a, None, None))))
        if str(v_a)[0: 2] == "00":
            break

    n = {
            "time": v_i["time"],
            "alg": v_i["alg"],
            "sig": encryption(v_i, None, e),
            "elapsed": int(time.time() * 1000) - v_o,
            "shaOne": v_a
    }

    return n
