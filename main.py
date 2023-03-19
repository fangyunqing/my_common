if __name__ == "__main__":




    def f(t):
        e = [0 for index in range(0, (len(t) >> 2) + 1)]
        for index in range(0, len(t) * 8, 8):
            e[index >> 5] |= (255 & ord(t[index // 8])) << index % 32
        return e


    values = {
        "alg": "v3",
        "apiver": "v3",
        "class": "login",
        "gid": "7F4118F-03A4-4E4C-B2A9-9FB843FA9D6B",
        "logintype": "dialogLogin",
        "loginversion": "v4",
        "subpro": "",
        "time": 1679202512,
        "token": "",
        "tpl": "ik",
        "tt": 1679202480912
    }

    i = "&".join([f"{k}={v}" for k, v in values.items()])
    c(f(i), len(i) * 8)
