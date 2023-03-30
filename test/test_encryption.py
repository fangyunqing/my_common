import base64
import unittest
from original.encryption import encryption


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
