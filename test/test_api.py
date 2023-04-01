# @Time    : 2023/03/31 9:52
# @Author  : fyq
# @File    : test_api.py
# @Software: PyCharm

__author__ = 'fyq'

import unittest
import api


class TestApi(unittest.TestCase):

    def test_get_api(self):
        res = api.get_api_info()
        print(res)
