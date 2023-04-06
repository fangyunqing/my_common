from original.default_list import DefaultList
from util import unsigned_right_shift, left_shift


def _u(t, r):
    """
        function u(t, r) {
            var e = (65535 & t) + (65535 & r);
            return (t >> 16) + (r >> 16) + (e >> 16) << 16 | 65535 & e
        }
    """
    t = t if t else 0
    e = (65535 & t) + (65535 & r)
    return left_shift((t >> 16) + (r >> 16) + (e >> 16), 16) | 65535 & e


def _s(t, r, e, n, i, o):
    """
        function s(t, r, e, n, i, o) {
            return u(function a(t, r) {
                return t << r | t >>> 32 - r
            }(u(u(r, t), u(n, o)), i), e)
        }
    """

    def a(_t, _r):
        return left_shift(_t, _r) | unsigned_right_shift(_t, 32 - _r)

    return _u(a(_u(_u(r, t), _u(n, o)), i), e)


def _l(t, r, e, n, i, o, a):
    """
        function l(t, r, e, n, i, o, a) {
            return s(r & e | ~r & n, t, r, i, o, a)
        }
    """
    return _s(r & e | ~r & n, t, r, i, o, a)


def _d(t, r, e, n, i, o, a):
    """
        function d(t, r, e, n, i, o, a) {
            return s(r & n | e & ~n, t, r, i, o, a)
        }
    """
    return _s(r & n | e & ~n, t, r, i, o, a)


def _p(t, r, e, n, i, o, a):
    """
        function p(t, r, e, n, i, o, a) {
            return s(r ^ e ^ n, t, r, i, o, a)
        }
    """
    return _s(r ^ e ^ n, t, r, i, o, a)


def _v(t, r, e, n, i, o, a):
    """
        function v(t, r, e, n, i, o, a) {
            return s(e ^ (r | ~n), t, r, i, o, a)
        }
    """
    return _s(e ^ (r | ~n), t, r, i, o, a)


def c(t, r):
    """
        function c(t, r) {
            t[r >> 5] |= 128 << r % 32,
            t[14 + (r + 64 >>> 9 << 4)] = r;
            var e, n, i, o, a, s = 1732584193, c = -271733879, h = -1732584194, f = 271733878;
            for (e = 0; e < t.length; e += 16)
                c = v(c = v(c = v(c = v(c = p(c = p(c = p(c = p(c = d(c = d(c = d(c = d(c = l(c = l(c = l(c = l(i = c, h = l(o = h, f = l(a = f, s = l(n = s, c, h, f, t[e], 7, -680876936), c, h, t[e + 1], 12, -389564586), s, c, t[e + 2], 17, 606105819), f, s, t[e + 3], 22, -1044525330), h = l(h, f = l(f, s = l(s, c, h, f, t[e + 4], 7, -176418897), c, h, t[e + 5], 12, 1200080426), s, c, t[e + 6], 17, -1473231341), f, s, t[e + 7], 22, -45705983), h = l(h, f = l(f, s = l(s, c, h, f, t[e + 8], 7, 1770035416), c, h, t[e + 9], 12, -1958414417), s, c, t[e + 10], 17, -42063), f, s, t[e + 11], 22, -1990404162), h = l(h, f = l(f, s = l(s, c, h, f, t[e + 12], 7, 1804603682), c, h, t[e + 13], 12, -40341101), s, c, t[e + 14], 17, -1502002290), f, s, t[e + 15], 22, 1236535329), h = d(h, f = d(f, s = d(s, c, h, f, t[e + 1], 5, -165796510), c, h, t[e + 6], 9, -1069501632), s, c, t[e + 11], 14, 643717713), f, s, t[e], 20, -373897302), h = d(h, f = d(f, s = d(s, c, h, f, t[e + 5], 5, -701558691), c, h, t[e + 10], 9, 38016083), s, c, t[e + 15], 14, -660478335), f, s, t[e + 4], 20, -405537848), h = d(h, f = d(f, s = d(s, c, h, f, t[e + 9], 5, 568446438), c, h, t[e + 14], 9, -1019803690), s, c, t[e + 3], 14, -187363961), f, s, t[e + 8], 20, 1163531501), h = d(h, f = d(f, s = d(s, c, h, f, t[e + 13], 5, -1444681467), c, h, t[e + 2], 9, -51403784), s, c, t[e + 7], 14, 1735328473), f, s, t[e + 12], 20, -1926607734), h = p(h, f = p(f, s = p(s, c, h, f, t[e + 5], 4, -378558), c, h, t[e + 8], 11, -2022574463), s, c, t[e + 11], 16, 1839030562), f, s, t[e + 14], 23, -35309556), h = p(h, f = p(f, s = p(s, c, h, f, t[e + 1], 4, -1530992060), c, h, t[e + 4], 11, 1272893353), s, c, t[e + 7], 16, -155497632), f, s, t[e + 10], 23, -1094730640), h = p(h, f = p(f, s = p(s, c, h, f, t[e + 13], 4, 681279174), c, h, t[e], 11, -358537222), s, c, t[e + 3], 16, -722521979), f, s, t[e + 6], 23, 76029189), h = p(h, f = p(f, s = p(s, c, h, f, t[e + 9], 4, -640364487), c, h, t[e + 12], 11, -421815835), s, c, t[e + 15], 16, 530742520), f, s, t[e + 2], 23, -995338651), h = v(h, f = v(f, s = v(s, c, h, f, t[e], 6, -198630844), c, h, t[e + 7], 10, 1126891415), s, c, t[e + 14], 15, -1416354905), f, s, t[e + 5], 21, -57434055), h = v(h, f = v(f, s = v(s, c, h, f, t[e + 12], 6, 1700485571), c, h, t[e + 3], 10, -1894986606), s, c, t[e + 10], 15, -1051523), f, s, t[e + 1], 21, -2054922799), h = v(h, f = v(f, s = v(s, c, h, f, t[e + 8], 6, 1873313359), c, h, t[e + 15], 10, -30611744), s, c, t[e + 6], 15, -1560198380), f, s, t[e + 13], 21, 1309151649), h = v(h, f = v(f, s = v(s, c, h, f, t[e + 4], 6, -145523070), c, h, t[e + 11], 10, -1120210379), s, c, t[e + 2], 15, 718787259), f, s, t[e + 9], 21, -343485551),
                s = u(s, n),
                c = u(c, i),
                h = u(h, o),
                f = u(f, a);
            return [s, c, h, f]
        }
    """
    t[r >> 5] |= left_shift(128, r % 32)
    location = 14 + left_shift(unsigned_right_shift (r + 64, 9), 4)
    while len(t) < location + 1:
        t.append(0)
    t[location] = r

    t = DefaultList(t)

    v_s = 1732584193
    v_c = -271733879
    v_h = -1732584194
    v_f = 271733878

    for e in range(0, len(t), 16):
        v_i = v_c
        v_o = v_h
        v_a = v_f
        v_n = v_s

        v_s = _l(v_n, v_c, v_h, v_f, t[e], 7, -680876936)
        v_f = _l(v_a, v_s, v_c, v_h, t[e + 1], 12, -389564586)
        v_h = _l(v_o, v_f, v_s, v_c, t[e + 2], 17, 606105819)
        v_c = _l(v_i, v_h, v_f, v_s, t[e + 3], 22, -1044525330)

        v_s = _l(v_s, v_c, v_h, v_f, t[e + 4], 7, -176418897)
        v_f = _l(v_f, v_s, v_c, v_h, t[e + 5], 12, 1200080426)
        v_h = _l(v_h, v_f, v_s, v_c, t[e + 6], 17, -1473231341)
        v_c = _l(v_c, v_h, v_f, v_s, t[e + 7], 22, -45705983)

        v_s = _l(v_s, v_c, v_h, v_f, t[e + 8], 7, 1770035416)
        v_f = _l(v_f, v_s, v_c, v_h, t[e + 9], 12, -1958414417)
        v_h = _l(v_h, v_f, v_s, v_c, t[e + 10], 17, -42063)
        v_c = _l(v_c, v_h, v_f, v_s, t[e + 11], 22, -1990404162)

        v_s = _l(v_s, v_c, v_h, v_f, t[e + 12], 7, 1804603682)
        v_f = _l(v_f, v_s, v_c, v_h, t[e + 13], 12, -40341101)
        v_h = _l(v_h, v_f, v_s, v_c, t[e + 14], 17, -1502002290)
        v_c = _l(v_c, v_h, v_f, v_s, t[e + 15], 22, 1236535329)

        v_s = _d(v_s, v_c, v_h, v_f, t[e + 1], 5, -165796510)
        v_f = _d(v_f, v_s, v_c, v_h, t[e + 6], 9, -1069501632)
        v_h = _d(v_h, v_f, v_s, v_c, t[e + 11], 14, 643717713)
        v_c = _d(v_c, v_h, v_f, v_s, t[e], 20, -373897302)

        v_s = _d(v_s, v_c, v_h, v_f, t[e + 5], 5, -701558691)
        v_f = _d(v_f, v_s, v_c, v_h, t[e + 10], 9, 38016083)
        v_h = _d(v_h, v_f, v_s, v_c, t[e + 15], 14, -660478335)
        v_c = _d(v_c, v_h, v_f, v_s, t[e + 4], 20, -405537848)

        v_s = _d(v_s, v_c, v_h, v_f, t[e + 9], 5, 568446438)
        v_f = _d(v_f, v_s, v_c, v_h, t[e + 14], 9, -1019803690)
        v_h = _d(v_h, v_f, v_s, v_c, t[e + 3], 14, -187363961)
        v_c = _d(v_c, v_h, v_f, v_s, t[e + 8], 20, 1163531501)

        v_s = _d(v_s, v_c, v_h, v_f, t[e + 13], 5, -1444681467)
        v_f = _d(v_f, v_s, v_c, v_h, t[e + 2], 9, -51403784)
        v_h = _d(v_h, v_f, v_s, v_c, t[e + 7], 14, 1735328473)
        v_c = _d(v_c, v_h, v_f, v_s, t[e + 12], 20, -1926607734)

        v_s = _p(v_s, v_c, v_h, v_f, t[e + 5], 4, -378558)
        v_f = _p(v_f, v_s, v_c, v_h, t[e + 8], 11, -2022574463)
        v_h = _p(v_h, v_f, v_s, v_c, t[e + 11], 16, 1839030562)
        v_c = _p(v_c, v_h, v_f, v_s, t[e + 14], 23, -35309556)

        v_s = _p(v_s, v_c, v_h, v_f, t[e + 1], 4, -1530992060)
        v_f = _p(v_f, v_s, v_c, v_h, t[e + 4], 11, 1272893353)
        v_h = _p(v_h, v_f, v_s, v_c, t[e + 7], 16, -155497632)
        v_c = _p(v_c, v_h, v_f, v_s, t[e + 10], 23, -1094730640)

        v_s = _p(v_s, v_c, v_h, v_f, t[e + 13], 4, 681279174)
        v_f = _p(v_f, v_s, v_c, v_h, t[e], 11, -358537222)
        v_h = _p(v_h, v_f, v_s, v_c, t[e + 3], 16, -722521979)
        v_c = _p(v_c, v_h, v_f, v_s, t[e + 6], 23, 76029189)

        v_s = _p(v_s, v_c, v_h, v_f, t[e + 9], 4, -640364487)
        v_f = _p(v_f, v_s, v_c, v_h, t[e + 12], 11, -421815835)
        v_h = _p(v_h, v_f, v_s, v_c, t[e + 15], 16, 530742520)
        v_c = _p(v_c, v_h, v_f, v_s, t[e + 2], 23, -995338651)

        v_s = _v(v_s, v_c, v_h, v_f, t[e], 6, -198630844)
        v_f = _v(v_f, v_s, v_c, v_h, t[e + 7], 10, 1126891415)
        v_h = _v(v_h, v_f, v_s, v_c, t[e + 14], 15, -1416354905)
        v_c = _v(v_c, v_h, v_f, v_s, t[e + 5], 21, -57434055)

        v_s = _v(v_s, v_c, v_h, v_f, t[e + 12], 6, 1700485571)
        v_f = _v(v_f, v_s, v_c, v_h, t[e + 3], 10, -1894986606)
        v_h = _v(v_h, v_f, v_s, v_c, t[e + 10], 15, -1051523)
        v_c = _v(v_c, v_h, v_f, v_s, t[e + 1], 21, -2054922799)

        v_s = _v(v_s, v_c, v_h, v_f, t[e + 8], 6, 1873313359)
        v_f = _v(v_f, v_s, v_c, v_h, t[e + 15], 10, -30611744)
        v_h = _v(v_h, v_f, v_s, v_c, t[e + 6], 15, -1560198380)
        v_c = _v(v_c, v_h, v_f, v_s, t[e + 13], 21, 1309151649)

        v_s = _v(v_s, v_c, v_h, v_f, t[e + 4], 6, -145523070)
        v_f = _v(v_f, v_s, v_c, v_h, t[e + 11], 10, -1120210379)
        v_h = _v(v_h, v_f, v_s, v_c, t[e + 2], 15, 718787259)
        v_c = _v(v_c, v_h, v_f, v_s, t[e + 9], 21, -343485551)

        v_s = _u(v_s, v_n)
        v_c = _u(v_c, v_i)
        v_h = _u(v_h, v_o)
        v_f = _u(v_f, v_a)

    return [v_s, v_c, v_h, v_f]


def f(t):
    e = [0 for index in range(0, (len(t) >> 2) + 1)]
    for index in range(0, len(t) * 8, 8):
        e[index >> 5] |= left_shift((255 & ord(t[index // 8])), index % 32)
    return e


def h(t):
    """
        function h(t) {
            var r, e = "";
            for (r = 0; r < 32 * t.length; r += 8)
                e += String.fromCharCode(t[r >> 5] >>> r % 32 & 255);
            return e
        }
    """
    e = ""
    for r in range(0, len(t) * 32, 8):
        e += chr(unsigned_right_shift(t[r >> 5], r % 32) & 255)
    return e


def f_o(t):
    """
       function o(t) {
        var r, e, n = "0123456789abcdef", i = "";
        for (e = 0; e < t.length; e += 1)
            r = t.charCodeAt(e),
            i += n.charAt(r >>> 4 & 15) + n.charAt(15 & r);
        return i
    }
    """
    n = "0123456789abcdef"
    i = ""
    for e in range(0, len(t)):
        r = ord(t[e])
        i += n[unsigned_right_shift(r, 4) & 15] + n[15 & r]
    return i


def _(t, r):
    """
        function _(t, r) {
            return function s(t, r) {
                var e, n, i = f(t), o = [], a = [];
                for (o[15] = a[15] = undefined,
                16 < i.length && (i = c(i, 8 * t.length)),
                e = 0; e < 16; e += 1)
                    o[e] = 909522486 ^ i[e],
                    a[e] = 1549556828 ^ i[e];
                return n = c(o.concat(f(r)), 512 + 8 * r.length),
                h(c(a.concat(n), 640))
            }(e(t), e(r))
        }
    """
    return []


def f_e(t):
    """
        function e(t) {
            return unescape(encodeURIComponent(t))
        }
    """
    return t


def f_a(t):
    """
        function a(t) {
            return function r(t) {
                return h(c(f(t), 8 * t.length))
            }(e(t))
        }
    """
    def func(v_t):
        return h(c(f(v_t), 8 * len(v_t)))
    return func(str(t))


def g(t, r, e):
    """
        t.exports = function g(t, r, e) {
            return r ? e ? _(r, t) : function n(t, r) {
                return o(_(t, r))
            }(r, t) : e ? a(t) : function i(t) {
                return o(a(t))
            }(t)
    """
    if r:
        if e:
            return _(r, t)
        else:
            return f_o(_(r, t))
    else:
        if e:
            return f_a(t)
        else:
            return f_o(f_a(t))
