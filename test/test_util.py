# @Time    : 2023/04/06 16:21
# @Author  : fyq
# @File    : test_util.py
# @Software: PyCharm

__author__ = 'fyq'

import unittest

import util


class TestUtil(unittest.TestCase):

    def test_create_page_token(self):

        print(util.create_page_token())