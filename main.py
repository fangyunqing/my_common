import random
import string

import requests

from api import get_api_info, get_public_key
import json

headers = {
    "Host": "passport.baidu.com",
    "Referer": "https://zhidao.baidu.com/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

session = requests.session()
session.headers = headers
session.get("https://www.baidu.com", )

res_dict = get_api_info(session)

res_dict = get_public_key(session)
