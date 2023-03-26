from original.default_list import DefaultList
from original.util import left_shift, unsigned_right_shift

a = 0


def o(t):
    """
        function o(t) {
            for (var r = 1 + (t.length + 8 >> 6), e = new Array(16 * r), n = 0; n < 16 * r; n++)
                e[n] = 0;
            for (n = 0; n < t.length; n++)
                e[n >> 2] |= t.charCodeAt(n) << 24 - 8 * (3 & n);
            return e[n >> 2] |= 128 << 24 - 8 * (3 & n),
            e[16 * r - 1] = 8 * t.length,
            e
        }
    """
    r = 1 + (len(t) + 8 >> 6)
    e = [0 for index in range(0, 16 * r)]
    n = 0
    for n in range(0, len(t)):
        e[n >> 2] |= left_shift(ord(t[n]), 24 - 8 * (3 & n))
    n += 1
    e[n >> 2] |= left_shift(128, 24 - 8 * (3 & n))
    e[16 * r - 1] = 8 * len(t)
    return e


def g(t):
    """
        function g(t) {
            for (var r = t, e = Array(80), n = 1732584193, i = -271733879, o = -1732584194, a = 271733878, s = -1009589776, c = 0; c < r.length; c += 16) {
                for (var h = n, f = i, u = o, l = a, d = s, p = 0; p < 80; p++) {
                    e[p] = p < 16 ? r[c + p] : B(e[p - 3] ^ e[p - 8] ^ e[p - 14] ^ e[p - 16], 1);
                    var v = w(w(B(n, 5), y(p, i, o, a)), w(w(s, e[p]), (_ = p) < 20 ? 1518500249 : _ < 40 ? 1859775393 : _ < 60 ? -1894007588 : -899497514));
                    s = a,
                    a = o,
                    o = B(i, 30),
                    i = n,
                    n = v
                }
                n = w(n, h),
                i = w(i, f),
                o = w(o, u),
                a = w(a, l),
                s = w(s, d)
            }
            var _;
            return new Array(n,i,o,a,s)
        }
    """
    r = DefaultList(t)
    e = [0 for index in range(0, 80)]
    n = 1732584193
    i = -271733879
    v_o = -1732584194
    a = 271733878
    s = -1009589776
    for c in range(0, len(r), 16):
        h = n
        f = i
        u = v_o
        v_l = a
        d = s
        for p in range(0, 80):
            e[p] = r[c + p] if p < 16 else b(e[p - 3] ^ e[p - 8] ^ e[p - 14] ^ e[p - 16], 1)
            var1 = w(b(n, 5), y(p, i, v_o, a))
            _ = p
            if _ < 20:
                vv = 1518500249
            elif _ < 40:
                vv = 1859775393
            elif _ < 60:
                vv = -1894007588
            else:
                vv = -899497514
            var2 = w(w(s, e[p]), vv)
            v = w(var1, var2)
            s = a
            a = v_o
            v_o = b(i, 30)
            i = n
            n = v
        n = w(n, h)
        i = w(i, f)
        v_o = w(v_o, u)
        a = w(a, v_l)
        s = w(s, d)
    return [n, i, v_o, a, s]


def b(t, r):
    return left_shift(t, r) | unsigned_right_shift(t, 32 - r)


def w(t, r):
    """
    function w(t, r) {
        var e = (65535 & t) + (65535 & r);
        return (t >> 16) + (r >> 16) + (e >> 16) << 16 | 65535 & e
    }
    """
    e = (65535 & t) + (65535 & r)
    return left_shift((t >> 16) + (r >> 16) + (e >> 16), 16) | 65535 & e


def y(t, r, e, n):
    """
    function y(t, r, e, n) {
        return t < 20 ? r & e | ~r & n : t < 40 ? r ^ e ^ n : t < 60 ? r & e | r & n | e & n : r ^ e ^ n
    }
    """
    if t < 20:
        return r & e | ~r & n
    elif t < 40:
        return r ^ e ^ n
    elif t < 60:
        return r & e | r & n | e & n
    return r ^ e ^ n


def i(t):
    """
    function i(t) {
            for (var r = a ? "0123456789ABCDEF" : "0123456789abcdef", e = "", n = 0; n < 4 * t.length; n++)
                e += r.charAt(t[n >> 2] >> 8 * (3 - n % 4) + 4 & 15) + r.charAt(t[n >> 2] >> 8 * (3 - n % 4) & 15);
        return e
    }
    """
    if a:
        r = "0123456789ABCDEF"
    else:
        r = "0123456789abcdef"
    e = ""
    for n in range(0, 4 * len(t)):
        e += r[t[n >> 2] >> 8 * (3 - n % 4) + 4 & 15] + r[t[n >> 2] >> 8 * (3 - n % 4) & 15]
    return e

