import random
import string

import requests

from api import get_api_info


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


headers = {
    "Host": "passport.baidu.com",
    "Referer": "https://zhidao.baidu.com/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

session = requests.session()
session.headers = headers
session.get("https://www.baidu.com", )

call_back_name = random_callback()
response = session.get(get_api_info() + pack_callback(call_back_name))
