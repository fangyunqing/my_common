from original.default_list import DefaultList
import original.func1 as o_func1

_d = d = {
    "a": "3",
    "b": "4",
    "c": "5",
    "d": "9",
    "e": "8",
    "f": "7",
    "g": "1",
    "h": "2",
    "i": "6",
    "j": "0",
    "k": "a",
    "l": "b",
    "m": "c",
    "n": "d",
    "o": "e",
    "p": "f",
    "q": "g",
    "r": "z",
    "s": "y",
    "t": "x",
    "u": "w",
    "v": "v",
    "w": "u",
    "x": "o",
    "y": "p",
    "z": "q",
    "0": "s",
    "1": "t",
    "2": "r",
    "3": "h",
    "4": "i",
    "5": "j",
    "6": "k",
    "7": "l",
    "8": "m",
    "9": "n"
}


def o(t, r):
    """
    function(t, r) {
        var e = [];
        for (var n in t)
            t.hasOwnProperty(n) && e.push(n);
        e.sort();
        for (var i = [], o = 0, a = e.length; o < a; o++) {
            var s = e[o];
            i.push(s + "=" + t[s])
        }
        var c = l(i.join("&"))
          , h = ""
          , f = (window.screen.width + "" + window.screen.height).split("");
        for (o = 0; o < f.length; o++)
            h += d[f[o]];
        return function u(t, r) {
            var e, n = "", i = t.split(""), o = r.split("");
            if (i.length >= o.length) {
                for (e = 0; e < o.length; e++)
                    n += i[e] + o[e];
                n += t.substring(e)
            } else {
                for (e = 0; e < i.length; e++)
                    n += i[e] + o[e];
                n += r.substring(e)
            }
            return n
        }(c, h)
    }
    """
    e = DefaultList(list(t.keys()))
    e.sort()
    i = []
    for s in e:
        i.append(f"{s}={t[s]}")
    c = o_func1.g("&".join(i), None, None)
    h = ""
    f = ["1", "3", "6", "6", "7", "6", "8"]
    for v_o in range(0, len(f)):
        h += _d[f[v_o]]

    return _u(c, h)


def _u(t: str, r: str):
    """
    function u(t, r) {
            var e, n = "", i = t.split(""), o = r.split("");
            if (i.length >= o.length) {
                for (e = 0; e < o.length; e++)
                    n += i[e] + o[e];
                n += t.substring(e)
            } else {
                for (e = 0; e < i.length; e++)
                    n += i[e] + o[e];
                n += r.substring(e)
            }
            return n
    }
    """
    n = ""
    i = t
    v_o = r
    if len(i) >= len(v_o):
        for e in range(0, len(v_o)):
            n += i[e] + v_o[e]
        n += t[len(v_o):]
    else:
        for e in range(0, len(i)):
            n += i[e] + v_o[e]
        n += t[len(i):]
    return n
