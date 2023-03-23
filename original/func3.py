# @Time    : 2023/03/21 20:08
# @Author  : fyq
# @File    : func3.py
# @Software: PyCharm

__author__ = 'fyq'

import time


def jsonp(n, i, s):
    """
            n.jsonp = function(n, i, s) {
                s = s || {},
                e && e.traceID && e.traceID.createTraceID && (i.traceid = e.traceID.createTraceID());
                var o = {};
                for (var a in i) {
                    var c = i[a];
                    void 0 !== c && null !== c && (o[a] = c)
                }
                try {
                    var l = "OOOO00"
                      , d = "OOO00O"
                      , g = "OOO000"
                      , p = "OOO0OO"
                      , m = "O0OOO0"
                      , f = {
                        OOOOO0: l,
                        O00000: d,
                        O0O00O: g,
                        O000OO: p,
                        O0O000: m
                    }
                      , h = (new Date).getTime() / 1e3
                      , v = parseInt(h / 86400, 10) % 5
                      , b = [];
                    if (Object && Object.keys)
                        b = Object.keys(f);
                    else {
                        b = [];
                        for (var y in f)
                            b.push(y)
                    }
                    var _ = f[b[v]] || "";
                    window.moonshadV3 && window.moonshadV3[_] && i && (i = baidu.extend(i, window.moonshadV3[_](o, baidu)))
                } catch (w) {
                    console.log(w)
                }
                return new t(function(e, t) {
                    n = r(n, i),
                    u(n, function(t) {
                        s.processData && (t = s.processData(t)),
                        e && e(t)
                    }, {
                        charset: s.charset,
                        queryField: s.queryField,
                        timeOut: s.timeOut,
                        onfailure: function() {
                            t && t()
                        }
                    })
                }
                )
            }
    """
    s = s if s else {}
    i["traceid"] = ""
    o = {}
    for k, v in i.items():
        if k:
            o[k] = v

    l = "OOOO00"
    d = "OOO00O"
    g = "OOO000"
    p = "OOO0OO"
    m = "O0OOO0"

    f = {
        "OOOOO0": l,
        "O00000": d,
        "O0O00O": g,
        "O000OO": p,
        "O0O000": m
    }

    h = int(time.time() * 1000) / 1000
    v = int(h / 86400) % 5
    b = list(f.keys())
    _ = ""
    if v < len(b):
        _ = f[b[v]]


