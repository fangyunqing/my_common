import unittest

from original.func6 import o

class TestFunc6(unittest.TestCase):

    def test_o(self):
        t = {
            "alg": "v3",
            "apiver": "v3",
            "gid": "C79D323-C73C-4284-A344-604D2D7BFFF2",
            "loginversion": "v5",
            "subpro": "",
            "time": 1679813244,
            "token": "",
            "tpl": "ik",
            "tt": 1679813159597
        }

        o(t, None)
