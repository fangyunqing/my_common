import operator
import unittest

from original.func1 import f_o, f


class TestFunc1(unittest.TestCase):

    def test_o(self):

        t = "ïhfé±Ì\u0018VþP&ÙZ}\u001b"
        self.assertEqual(f_o(t), "ef6866e9b1cc1856fe509f26d95a7d1b")

    def test_f(self):
        t = "1679620285240"
        res = [959919665, 842019382, 875705656, 48]
        self.assertTrue(operator.eq(res, f(t)))

