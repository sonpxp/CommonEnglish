import json
import re
import urllib.request
from bs4 import BeautifulSoup

urls = 'http://tratu.coviet.vn/hoc-tieng-anh/cau-truc-cau-tieng-anh-thong-dung/vietgle-tra-tu/tat-ca/trang-1.html'

page = urllib.request.urlopen(urls)
soup = BeautifulSoup(page, 'html.parser')
content = soup.find_all('ul', {'class': 'ucttatd ovf'})
english_phrases = []


def upper_case(s):
    return re.sub("(^|[.?!])\s*(.)", lambda p: p.group(0).upper(), s)


def replace_char(s):
    return re.sub("([/-])\s*", ', ', s)


for data in content:
    # print(data.text)
    item_phrase = {}
    mini_ex = {}
    example = []

    phrase_1 = data.find('span', class_='ctk').text
    mean_1 = data.find('span', class_='p5l cB').text
    en_1 = data.find('li', class_='icham m5t ctk').text
    vi_1 = data.find('li', class_='p10l').text

    phrase = upper_case(phrase_1)
    mean = upper_case(mean_1.replace(";", ","))
    en = upper_case(en_1)
    vi = upper_case(vi_1)

    mini_ex['en'] = en
    mini_ex['vi'] = vi
    example.append(mini_ex)

    item_phrase["phrase"] = phrase
    item_phrase["mean"] = mean
    item_phrase["example"] = example

    english_phrases.append(item_phrase)

with open('phrase_dict.json', 'w', encoding='utf-8') as f:
    json.dump(english_phrases, f, ensure_ascii=False, indent=4)

# (^|[.?!]) matches the start of the string ^ or .?! followed by optional spaces
# [a-zA-Z] matches letter directly after the first pattern
# use lambda function to convert the captured group to upper case
# re.sub("(^|[.?!])\s*([a-zA-Z])", lambda p: p.group(0).upper(), s)
# re.sub("(^|[.?!])\s*(.)", lambda p: p.group(0).upper(), s) # upper cac ki tu unicode
