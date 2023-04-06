# @Time    : 2023/04/06 16:50
# @Author  : fyq
# @File    : func9.py
# @Software: PyCharm

__author__ = 'fyq'

from typing import List


def S(e, t):
    """
    function S(e, t) {
            var r = new n(t)
              , o = {
                flashInfo: 0,
                mouseDown: 1,
                keyDown: 2,
                mouseMove: 3,
                version: 4,
                loadTime: 5,
                browserInfo: 6,
                token: 7,
                location: 8,
                screenInfo: 9
            }
              , a = [r.iary([2])];
            for (var i in e) {
                var d = e[i];
                if (void 0 !== d && void 0 !== o[i]) {
                    var c;
                    "number" == typeof d ? (c = d >= 0 ? 1 : 2,
                    d = r.int(d)) : "boolean" == typeof d ? (c = 3,
                    d = r.int(d ? 1 : 0)) : "object" == typeof d && d instanceof Array ? (c = 4,
                    d = r.bary(d)) : (c = 0,
                    d = r.str(d + "")),
                    d && a.push(r.iary([o[i], c, d.length]) + d)
                }
            }
            return a.join("")
        }
    """


def o(e: List[List]):
    """
    function o(e) {
        for (var t = [], n = 0; n < e.length; n++)
            for (var r = e[n][0]; r <= e[n][1]; r++)
                t.push(String.fromCharCode(r));
        return t
    }
    """
    t = []
    for v_n in range(0, len(e)):
        r_s = e[v_n][0]
        r_e = e[v_n][1]
        for v_r in range(r_s, r_e + 1):
            t.append(chr(v_r))
    return t


def r(e, t: str):
    """
    function r(e, t) {
        for (var n = t.split(""), r = 0; r < e.length; r++) {
            var o = r % n.length;
            o = n[o].charCodeAt(0),
            o %= e.length;
            var a = e[r];
            e[r] = e[o],
            e[o] = a
        }
        return e
    }
    """
    v_n = t.split()
    for v_r in range(0, len(e)):
        v_o = v_r % len(v_n)
        v_o = ord(v_n[v_o][0])
        v_o %= len(e)
        a = e[v_r]
        e[v_r] = e[v_o]
        e[v_o] = a
    return e


def n(e):
    """
    function n(e) {
        var t = [[48, 57], [65, 90], [97, 122], [45, 45], [126, 126]]
          , n = o(t)
          , a = o(t.slice(1));
        e && (n = r(n, e),
        a = r(a, e)),
        this.dict = n,
        this.dict2 = a
    }
    """
    t = [[48, 57], [65, 90], [97, 122], [45, 45], [126, 126]]
    v_n = o(t)
    a = o(t[1:])
    v_n = r(v_n, e)
    a = r(a, e)
    return {
        "dict": v_n,
        "dict2": a
    }
