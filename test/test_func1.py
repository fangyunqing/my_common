import operator
import unittest

from original.func1 import f_o, f, c, h


class TestFunc1(unittest.TestCase):

    def test_o(self):
        t = "ïhfé±Ì\u0018VþP&ÙZ}\u001b"
        self.assertEqual(f_o(t), "ef6866e9b1cc1856fe509f26d95a7d1b")

    def test_f(self):
        t = "1679661109435"
        res = [959919665, 943075383, 875638838, 49]
        self.assertTrue(operator.eq(res, f(t)))

    def test_c(self):
        t = [959919665, 943075383, 875638838, 49]
        r = len("1679661109435") * 8
        c(t, r)

    def test_h(self):
        t = [1312666516, 33184832, -1832418746, -418666474]
        e = "³=N@\\ú\u0001FÇ\u0016¨\u000bç"
        self.assertEqual(h(t), e)
