import unittest

from original.func5 import o


class TestFunc5(unittest.TestCase):

    def test_o(self):

        t = "ef6866e9b1cc1856fe509f26d95a7d1b"
        self.assertEqual(o(t), "ef6866e9b1cc1856fe509f26d95a7d1b")
