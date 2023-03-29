import unittest
from original.encryption import encryption


class TestEncryption(unittest.TestCase):

    def test_encryption(self):
        t = {
            "alg": "v3",
            "apiver": "v3",
            "class": "login",
            "gid": "675CAFF-D235-4D2A-8C3C-5EB3AAB14D58",
            "logintype": "dialogLogin",
            "loginversion": "v4",
            "subpro": "",
            "time": 1680092358,
            "token": "",
            "tpl": "ik",
            "tt": 1680092334549
        }

        e = "moonshad5moonsh2"
        res = encryption(t, None, e)
        self.assertEqual(res, "vDKn8KTg3Hk30YhOOcIGKf8tYN1D00v72BQJc/rQQBCtX/90eP9a+hyw30xmovLv")
