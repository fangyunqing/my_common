from original.util import left_shift


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
