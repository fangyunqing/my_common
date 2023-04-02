# @Time    : 2023/03/31 9:00
# @Author  : fyq
# @File    : func7.py
# @Software: PyCharm

__author__ = 'fyq'

from urllib.parse import quote


def a(e):
    """
    function(e) {
        if ("object" == typeof e) {
            var t = [];
            for (var n in e) {
                var i = e[n];
                if (void 0 !== i && null !== i) {
                    t.length && t.push("&");
                    var s = encodeURIComponent("boolean" == typeof i ? i ? "1" : "0" : i.toString());
                    t.push(encodeURIComponent(n), "=", s)
                }
            }
            return t.join("")
        }
        return "string" == typeof e ? e : null
    }
    """
    if isinstance(e, dict):
        t = []
        for k, v in e.items():
            if v is not None:
                if len(t) > 0:
                    t.append("&")
                if isinstance(v, bool):
                    s = "1" if v else "0"
                else:
                    s = str(v)
                t.append(quote(k))
                t.append("=")
                t.append(quote(s))
        return "".join(t)
    return e if isinstance(e, str) else None


def r(e, t):
    t = a(t)
    if isinstance(t, str):
        if "?" in e:
            e += "&" + a(t)
        else:
            e += "?" + a(t)
    return e


