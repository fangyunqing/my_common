import unittest

from original.func1 import o


class TestFunc1(unittest.TestCase):

    def test_o(self):

        t = "ïhfé±Ì\u0018VþP&ÙZ}\u001b"
        self.assertEqual(o(t), "ef6866e9b1cc1856fe509f26d95a7d1b")

