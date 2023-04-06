import ctypes
import json
import random
import string
import time
import uuid
from typing import Dict


def unsigned_right_shift(n, i):
    def int_overflow(val):
        maxint = 2147483647
        if not -maxint - 1 <= val <= maxint:
            val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
        return val

    # 数字小于0，则转为32位无符号uint
    if n < 0:
        n = ctypes.c_uint32(n).value
    # 正常位移位数是为正数，但是为了兼容js之类的，负数就右移变成左移好了
    if i < 0:
        return -int_overflow(n << abs(i))
    return int_overflow(n >> i)


def left_shift(based, counter):
    if not based:
        return 0
    val = based << (counter % 32)
    maxint = 2147483647
    if not -maxint - 1 <= val <= maxint:
        val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
    return val


def _guid_random():
    guid = str(uuid.uuid4()).upper()
    return guid[1: len(guid)] + guid[0]


def random_callback(rule="??__???__??????"):
    res = ""
    for index, r in enumerate(rule):
        if r == "?":
            if index in [0, 1] or random.randint(0, 1) == 0:
                res += random.choice(string.ascii_lowercase)
            else:
                res += str(int(random.random() * 10))
        else:
            res += r
    return res


def pack_callback(call_back):
    return "&call_back=" + call_back


def jquery_random_call_back():
    """
        jQuery110207053490627294874_1680752947519
    """
    res = "jQuery"
    for n in range(0, 21):
        res += str(int(random.random() * 10))
    res += f"_{int(time.time() * 1000)}"

    return res


def replace_text2dict(response_text: str, callback_name: str) -> Dict:
    response_text = response_text.replace(callback_name, "")
    if response_text.startswith("("):
        response_text = response_text[1:]
    if response_text.endswith(")"):
        response_text = response_text[0:len(response_text) - 1]
    return json.loads(response_text)


def create_page_token():
    r = str(random.random())
    r = r[0:18]
    while len(r) < 18:
        r += str(int(random.random() * 10))
    return f"tk{r}{int(time.time() * 1000)}"
