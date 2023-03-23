import unittest

from original.func2 import i


class TestFunc2(unittest.TestCase):

    def test_i(self):

        e = {
            "apiType": "login",
            "gid": "1A3E576-22A7-4CB5-BC8D-1C0D4570F1C7",
            "loginType": "dialogLogin",
            "loginVersion": "v4"
        }

        t = "getApiInfo"

        n = {"apiType": "class"}

        r = None

        s = False

        self.assertEqual(len(i(e, t, n, r, s)), 9)


