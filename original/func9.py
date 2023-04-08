# @Time    : 2023/04/06 16:50
# @Author  : fyq
# @File    : func9.py
# @Software: PyCharm

__author__ = 'fyq'

import math
from typing import List

from util import left_shift


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
    v_r = n(t)
    v_o = {
        "flashInfo": 0,
        "mouseDown": 1,
        "keyDown": 2,
        "mouseMove": 3,
        "version": 4,
        "loadTime": 5,
        "browserInfo": 6,
        "token": 7,
        "location": 8,
        "screenInfo": 9
    }
    v_a = [_iary([2], v_r.get("dict2"))]
    for i in e:
        d = e[i]
        if d is not None and i in v_o:
            if isinstance(d, int) or isinstance(d, float):
                if d >= 0:
                    v_c = 1
                else:
                    v_c = 2
                d = _int(d, v_r.get("dict"))
            elif isinstance(d, bool):
                v_c = 3
                d = _int(1 if d else 0, v_r.get("dict"))
            elif isinstance(d, list):
                v_c = 4
                d = _bary(d, v_r.get("dict"))
            else:
                v_c = 0
                d = _str(str(d), v_r.get("dict"))
            if d:
                v_a.append(_iary([v_o[i], v_c, len(d)], v_r.get("dict2")) + d)
    return "".join(v_a)


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


def a(e, t):
    """
    function a(e, t) {
        var n = ""
          , r = Math.abs(parseInt(e));
        if (r)
            for (; r; )
                n += t[r % t.length],
                r = parseInt(r / t.length);
        else
            n = t[0];
        return n
    }
    """
    v_n = ""
    v_r = abs(int(e))
    if v_r:
        while v_r != 0:
            v_n += t[v_r % len(t)]
            v_r = int(v_r / len(t))
    else:
        v_n = t[0]
    return v_n


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
    v_n = t
    for v_r in range(0, len(e)):
        v_o = v_r % len(v_n)
        v_o = ord(v_n[v_o][0])
        v_o %= len(e)
        v_a = e[v_r]
        e[v_r] = e[v_o]
        e[v_o] = v_a
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
    v_a = o(t[1:])
    v_n = r(v_n, e)
    v_a = r(v_a, e)
    res = {
        "dict": v_n,
        "dict2": v_a
    }
    return res


def _int(e, t):
    """
    "int": function(e) {
        return a(e, this.dict)
    },
    """
    return a(e, t)


def _iary(e, g):
    """
    iary: function(e) {
        for (var t = "", n = 0; n < e.length; n++) {
            var r = a(e[n], this.dict2);
            t += r.length > 1 ? r.length - 2 + r : r
        }
        return t
    },
    """
    t = ""
    for v_n in range(0, len(e)):
        v_r = a(e[v_n], g)
        t += len(v_r) - 2 + v_r if len(v_r) > 1 else v_r
    return t


def _bary(e, g):
    """
    bary: function(e) {
        for (var t = 0, n = {}, r = 0; r < e.length; r++)
            e[r] > t && (t = e[r],
            n[e[r]] = !0);
        var o = parseInt(t / 6);
        o += t % 6 ? 1 : 0;
        for (var a = "", r = 0; o > r; r++) {
            for (var i = 6 * r, d = 0, c = 0; 6 > c; c++)
                n[i] && (d += Math.pow(2, c)),
                i++;
            a += this.dict[d]
        }
        return a
    },
    """
    v_t = 0
    v_n = {}
    for v_r in range(0, len(e)):
        if e[v_r] > v_t:
            v_t = e[v_r]
            v_n[e[v_r]] = True
    v_o = int(v_t / 6)
    v_o += 1 if v_t % 6 else 0
    v_a = ""
    for v_r in range(0, v_o):
        v_i = 6 * v_r
        d = 0
        for c in range(0, 6):
            if v_n[v_i]:
                d += math.pow(2, c)
            v_i += 1
        v_a += g[d]
    return v_a


def _str(e, g):
    """
    str: function(e) {
        for (var t = [], n = 0; n < e.length; n++) {
            var r = e.charCodeAt(n);
            r >= 1 && 127 >= r ? t.push(r) : r > 2047 ? (t.push(224 | r >> 12 & 15),
            t.push(128 | r >> 6 & 63),
            t.push(128 | r >> 0 & 63)) : (t.push(192 | r >> 6 & 31),
            t.push(128 | r >> 0 & 63))
        }
        for (var o = "", n = 0, a = t.length; a > n; ) {
            var i = t[n++];
            if (n >= a) {
                o += this.dict[i >> 2],
                o += this.dict[(3 & i) << 4],
                o += "__";
                break
            }
            var d = t[n++];
            if (n >= a) {
                o += this.dict[i >> 2],
                o += this.dict[(3 & i) << 4 | (240 & d) >> 4],
                o += this.dict[(15 & d) << 2],
                o += "_";
                break
            }
            var c = t[n++];
            o += this.dict[i >> 2],
            o += this.dict[(3 & i) << 4 | (240 & d) >> 4],
            o += this.dict[(15 & d) << 2 | (192 & c) >> 6],
            o += this.dict[63 & c]
        }
        return o
    }
    """
    t = []
    for v_n in range(0, len(e)):
        v_r = ord(e[v_n])
        if 1 <= v_r <= 127:
            t.append(v_r)
        elif v_r > 2047:
            t.append(224 | v_r >> 12 & 15)
            t.append(128 | v_r >> 6 & 63)
            t.append(128 | v_r >> 0 & 63)
        else:
            t.append(192 | v_r >> 6 & 31)
            t.append(128 | v_r >> 0 & 63)
    v_o = ""
    v_n = 0
    v_a = len(t)
    while v_a > v_n:
        v_i = t[v_n]
        v_n += 1
        if v_n >= v_a:
            v_o += g[v_i >> 2]
            v_o += g[left_shift(3 & v_i, 4)]
            v_o += "__"
            break

        v_d = t[v_n]
        v_n += 1
        if v_n >= v_a:
            v_o += g[v_i >> 2]
            v_o += g[left_shift(3 & v_i, 4) | (240 & v_d) >> 4]
            v_o += g[left_shift(15 & v_d, 2)]
            v_o += "_"
            break

        v_c = t[v_n]
        v_n += 1
        v_o += g[v_i >> 2]
        v_o += g[left_shift(3 & v_i, 4) | (240 & v_d) >> 4]
        v_o += g[left_shift(15 & v_d, 2) | (192 & v_c) >> 6]
        v_o += g[63 & v_c]
    return v_o
