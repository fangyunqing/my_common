import base64
import unittest
from original.encryption import encryption, encryption1
from encryption import rsa


class TestEncryption(unittest.TestCase):

    def test_encryption(self):
        t = {
            "alg": "v3",
            "apiver": "v3",
            "gid": "23E9DA5-3EEF-4920-948A-489A8586D2E4",
            "loginversion": "v5",
            "subpro": "",
            "time": 1680136830,
            "token": "",
            "tpl": "ik",
            "tt": 1680136807207
        }

        e = "moonshad3moonsh0"
        res = encryption(t, None, e)
        print(res)
        print(base64.b64encode(res.encode()).decode())
        self.assertEqual(res, "vDKn8KTg3Hk30YhOOcIGKf8tYN1D00v72BQJc/rQQBCtX/90eP9a+hyw30xmovLv")

    def test_ras(self):
        key = '-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCv0vXk5tndH7ygeFiNi3t0BKfe' \
              '\ncrzzG99XjGbO0vqjE3xTJxOPenlvXVZH4LpPW\/yTraX0qQv14DKelmUfTxNweiZA' \
              '\njJB2EfX4ZHHbppucjaQatKsO0A5ouLO4glQGtiRZuVbxeN13b5E4FNVZ9+g8kj2e\nR9aWWBkFafs4d8tbtwIDAQAB\n-----END ' \
              'PUBLIC KEY-----\n '
        print(rsa.rsa(key, "fang353523500"))

    def test_encryption1(self):

        n = '{"cl":[{"x":453,"y":548,"t":1680743140416}],"mv":[{"fx":349,"fy":26,"t":1680743138782,"bf":2},{"fx":388,"fy":89,"t":1680743138934,"bf":2},{"fx":527,"fy":191,"t":1680743139087,"bf":2},{"fx":583,"fy":387,"t":1680743139823,"bf":2},{"fx":481,"fy":496,"t":1680743139982,"bf":2},{"fx":463,"fy":523,"t":1680743140134,"bf":2},{"fx":453,"fy":548,"t":1680743140287,"bf":2}],"sc":[{"tx":0,"ty":0}],"kb":[],"sb":[],"sd":[],"sm":[],"cr":{"screenTop":0,"screenLeft":0,"clientWidth":575,"clientHeight":918,"screenWidth":1920,"screenHeight":1080,"availWidth":1920,"availHeight":1040,"outerWidth":1920,"outerHeight":1040,"scrollWidth":1203,"scrollHeight":1203},"simu":0,"ac_c":0}'
        r = "85c7b2bdappsapi0"
        print(encryption1(n, r))