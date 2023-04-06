import base64

import original.func6 as o_func6
from encryption.ase import AESCryptor, MData
from Crypto.Cipher import AES

version = "v3"


def encryption(t, r, e):
    n = o_func6.o(t, r)
    aes = AESCryptor(e.encode(), AES.MODE_ECB, None, padding_mode="PKCS7Padding", character_set='utf-8')
    m_data = aes.encrypt_from_string(n)
    res = m_data.to_base64()
    return base64.b64encode(res.encode()).decode()


def encryption1(n, r):
    aes = AESCryptor(r.encode(), AES.MODE_ECB, None, padding_mode="PKCS7Padding", character_set='utf-8')
    m_data = aes.encrypt_from_string(n)
    res = m_data.to_base64()
    return res
