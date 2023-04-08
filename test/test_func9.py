# @Time    : 2023/04/07 16:37
# @Author  : fyq
# @File    : test_func9.py
# @Software: PyCharm

__author__ = 'fyq'

import unittest

from original.func9 import n, S


class TestFunc9(unittest.TestCase):

    def test_n(self):
        e = "tk0.67146330887275441680857124868"
        print(n(e))

    def test_S(self):
        e = {
            "mouseDown": "",
            "keyDown": "",
            "mouseMove": "",
            "version": 26,
            "loadTime": 1680916804.142,
            "browserInfo": "1,2,101",
            "token": "tk0.73967870619132241680916804142",
            "location": "https://zhidao.baidu.com/,undefined",
            "screenInfo": "0,0,205,2102,1920,1080,1920,1920,1040"
        }
        t = "tk0.73967870619132241680916804142"

        S(e, t)
