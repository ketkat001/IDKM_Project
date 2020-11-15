# -*- coding: utf-8 -*-
import requests
import json
import urllib.request as ul
import urllib
from collections import OrderedDict
from konlpy.utils import pprint
from konlpy.tag import Hannanum
from konlpy.tag import Kkma


with open('TMDB_Moviefinal.json', 'r', encoding='utf8') as f:
    movie = json.load(f)

A1 = OrderedDict()

m2 = []
for m in movie:
    if m['fields']['overview'] != '':
        A = m['fields']['title'] + ', ' + m['fields']['overview'] + ', ' + m['fields']['genres']
        m['fields']['searchdata'] = A
        m2.append(m)

with open('KMDB_Moviefinal.json', 'w', encoding="utf-8") as make_file:
    json.dump(m2, make_file, ensure_ascii=False, indent="\t")