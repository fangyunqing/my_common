# @Time    : 2023/04/04 16:43
# @Author  : fyq
# @File    : rsa.py
# @Software: PyCharm

__author__ = 'fyq'

import base64

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher


def rsa(public_key: str, data: str):
    public_key = RSA.importKey(public_key)
    cipher = PKCS1_cipher.new(public_key)
    encrypt_text = base64.b64encode(cipher.encrypt(data.encode()))
    return encrypt_text.decode()
