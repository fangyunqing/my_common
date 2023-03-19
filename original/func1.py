from original.util import unsigned_right_shift


def _u(t, r):
    e = (65535 & t) + (65535 & r)
    return (t >> 16) + (r >> 16) + (e >> 16) << 16 | 65535 & e


def _s(t, r, e, n, i, o):
    def a(_t, _r):
        return _t << _r | unsigned_right_shift(_t, 32) - _r
    return _u(a(_u(_u(t, r), _u(n, o)), i), e)


def _l(t, r, e, n, i, o, a):
    return _s(r & e | ~r & n, t, r, i, o, a)


def _d(t, r, e, n, i, o, a):
    return _s(r & n | e & ~n, t, r, i, o, a)


def _p(t, r, e, n, i, o, a):
    return _s(r ^ e ^ n, t, r, i, o, a)


def _v(t, r, e, n, i, o, a):
    return _s(e ^ (r | ~n), t, r, i, o, a)

   def c(t, r):
        t[r >> 5] |= 128 << r % 32
        location = 14 + (r + 64 >> 9 << 4)
        while len(t) < location + 1:
            t.append(None)
        t[location] = r

        v_s = 1732584193
        v_c = -271733879
        v_h = -1732584194
        v_f = 271733878
        v_n = 0
        v_a = 0
        v_i = 0
        v_o = 0
        for e in range(0, len(t) * 8, 16):
            v_i = v_c
            v_o = v_h
            v_a = v_f
            v_n = v_s

            v_s = _l(v_n, v_c, v_h, v_f, t[e], 7, -680876936)
            v_f = _l(v_a, v_s, v_c, v_h, t[e + 1], 12, -389564586)
            v_h = _l(v_o, v_f, v_s, v_c, t[e + 2], 17, 606105819)
            v_c = _l(v_i, v_h, v_f, v_s, t[e + 3], 22, -1044525330)

            v_s = _l(v_s, v_c, v_h, v_f, t[e + 4], 7, -176418897)
            v_f = _l(v_f, v_s ,v_c, v_h, t[e + 5], 12, 1200080426)
            v_h = _l(v_h, v_h, v_s, v_c, t[e + 6], 17, -1473231341)
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












            v_c = _v(v_c = _v(v_c = _v(c = _v(c = _p(c = _p(c = _p(c = _p(c = _d(c = _d(c = _d(c = _d(q), h = d(h, f = d(f, s = d(s, c, h, f, t[e + 5], 5, -701558691), c, h, t[e + 10], 9, 38016083), s, c, t[e + 15], 14, -660478335), f, s, t[e + 4], 20, -405537848), h = d(h, f = d(f, s = d(s, c, h, f, t[e + 9], 5, 568446438), c, h, t[e + 14], 9, -1019803690), s, c, t[e + 3], 14, -187363961), f, s, t[e + 8], 20, 1163531501), h = d(h, f = d(f, s = d(s, c, h, f, t[e + 13], 5, -1444681467), c, h, t[e + 2], 9, -51403784), s, c, t[e + 7], 14, 1735328473), f, s, t[e + 12], 20, -1926607734), h = p(h, f = p(f, s = p(s, c, h, f, t[e + 5], 4, -378558), c, h, t[e + 8], 11, -2022574463), s, c, t[e + 11], 16, 1839030562), f, s, t[e + 14], 23, -35309556), h = p(h, f = p(f, s = p(s, c, h, f, t[e + 1], 4, -1530992060), c, h, t[e + 4], 11, 1272893353), s, c, t[e + 7], 16, -155497632), f, s, t[e + 10], 23, -1094730640), h = p(h, f = p(f, s = p(s, c, h, f, t[e + 13], 4, 681279174), c, h, t[e], 11, -358537222), s, c, t[e + 3], 16, -722521979), f, s, t[e + 6], 23, 76029189), h = p(h, f = p(f, s = p(s, c, h, f, t[e + 9], 4, -640364487), c, h, t[e + 12], 11, -421815835), s, c, t[e + 15], 16, 530742520), f, s, t[e + 2], 23, -995338651), h = v(h, f = v(f, s = v(s, c, h, f, t[e], 6, -198630844), c, h, t[e + 7], 10, 1126891415), s, c, t[e + 14], 15, -1416354905), f, s, t[e + 5], 21, -57434055), h = v(h, f = v(f, s = v(s, c, h, f, t[e + 12], 6, 1700485571), c, h, t[e + 3], 10, -1894986606), s, c, t[e + 10], 15, -1051523), f, s, t[e + 1], 21, -2054922799), h = v(h, f = v(f, s = v(s, c, h, f, t[e + 8], 6, 1873313359), v_c, v_h, t[e + 15], 10, -30611744), v_s, v_c, t[e + 6], 15, -1560198380), v_f, v_s, t[e + 13], 21, 1309151649), h = v(v_h, f = v(v_f, s = _v(v_s, v_c, v_h, v_f, t[e + 4], 6, -145523070), v_c, v_h, t[e + 11], 10, -1120210379), v_s, v_c, t[e + 2], 15, 718787259), v_f, v_s, t[e + 9], 21, -343485551),



