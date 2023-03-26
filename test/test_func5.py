import unittest
import operator

from original.func5 import o, g, i
import original.func1 as o_func1


class TestFunc5(unittest.TestCase):

    def test_o(self):
        t = "fd04e7e4eefc63793154ca023e910fc2"
        e = [1717841972, 1698129204, 1701144163, 909326137, 858862900, 1667313714,
             862271793, 812016434, -2147483648, 0, 0, 0, 0, 0, 0, 256]
        self.assertTrue(operator.eq(o(t), e))

    def test_g(self):
        t = [1717841972, 1698129204, 1701144163, 909326137, 858862900, 1667313714,
             862271793, 812016434, -2147483648, 0, 0, 0, 0, 0, 0, 256]
        res = [-2037693903, -1869147764, 398193178, -19378648, -1836477622]
        self.assertTrue(operator.eq(g(t), res))

    def test_i(self):
        t = [-1707579758, 814806962, 849145295, -251099801, 1660199567]
        self.assertEqual(i(t), "9a3866923090f7b2329cedcff108856762f4a28f")

    def test_with_time(self):
        """
        for (o = a = (new Date).getTime(); "00" !== (a = l(d(a))).toString().substr(0, 2); )
                ;
        """
        v_o = 1679813243692
        a = v_o
        while True:
            a = i(g(o(o_func1.g(a, None, None))))
            if str(a)[0: 2] == "00":
                break
        print(a)