from original.util import unsigned_right_shift, left_shift
from original.func7.i import l


def parse(t):
    """
    function(t) {
        for (var r = t.length, e = [], n = 0; n < r; n++)
            e[n >>> 2] |= (255 & t.charCodeAt(n)) << 24 - n % 4 * 8;
    return new l.init(e,r)
    """
    r = len(t)
    d = {}
    for n in range(0, r):
        key = unsigned_right_shift(n, 2)
        d[key] = d.get(key, 0) | left_shift((255 & ord(t[n])), 24 - n % 4 * 8)

    e = list(d.keys())
    e.sort()
    for i in range(0, e[-1] + 1):
        if i in e:
            e[i] = d[i]
        else:
            e[i] = 0
    return l.init(e, r)



