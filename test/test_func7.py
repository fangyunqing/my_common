import unittest

from original.func7.i import utf8


class TestFunc6(unittest.TestCase):

    def test_i_utf8_parse(self):

        t = "moonshad0moonsh1"
        print(utf8.parse(t))

        r = "1ten4r5s7tas7m0s9932483543e2807f125918c6"
        print(utf8.parse(r))


