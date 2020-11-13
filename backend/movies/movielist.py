from konlpy.utils import pprint
import json
import urllib.request as ul
import urllib
from collections import OrderedDict
from konlpy.tag import Kkma

A = []
with open('TMDB_Moviefinal.json', 'r', encoding='utf8') as f:
    movie = json.load(f)


for m in movie:
    A.append(m['pk'])

with open('movie_list.json', 'w', encoding="utf-8") as make_file:
    json.dump(A, make_file, ensure_ascii=False, indent="\t")
