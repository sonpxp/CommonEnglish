import json

import requests
from bs4 import BeautifulSoup

url = 'https://giahanvisa.net.vn/tong-hop-gan-1000-cum-dong-tu-phrasal-verb-tieng-anh-thong-dung-tu-a-z/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40'}

response = requests.get(url, headers)
soup = BeautifulSoup(response.text, "html.parser")
data_div = soup.find_all('div', {'id': 'ftwp-postcontent'})
dic = {}  # dict


def convert(lst):
    it = iter(lst)
    res_dct = dict(zip(it, it))
    return res_dct


for data in data_div:
    for p in data.find_all('p')[5:1044]:
        # print(p.text.strip())
        data_tag = p.text  # lấy text trong thẻ tag <p>text</p>
        list_data = data_tag.split(': ')  # tách chuỗi(str)  -> list[]
        list_capitalize = list(map(lambda x: x.capitalize(), list_data))  # format chữ đầu viết hoa
        dict_convert = convert(list_capitalize)  # chuyển list[] -> dict{}
        dic.update(dict_convert)  # add dict
        # print(dic)

# print(dic)

with open('data_dict.json', 'w', encoding='utf-8') as f:
    json.dump(dic, f, ensure_ascii=False, indent=4)
