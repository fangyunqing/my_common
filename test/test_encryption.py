import base64
import unittest
from original.encryption import encryption
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
