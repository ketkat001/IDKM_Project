# -*- coding: utf-8 -*-
import requests
import json
import urllib.request as ul
import urllib
from collections import OrderedDict



# with open('KMDB_genre.json', 'r', encoding='utf8') as f:
#     json_data = json.load(f)
# A = OrderedDict()

# for j in json_data:
#     pk = j['pk']
#     name = j['fields']['genre']
#     A[name] = str(pk)
# with open('KMDB_genre_pk.json', 'w', encoding="utf-8") as make_file:
#     json.dump(A, make_file, ensure_ascii=False, indent="\t")



with open('KMDB_genre_pk.json', 'r', encoding='utf8') as f:
    gpk = json.load(f)

with open('KMDB_Moviefinal.json', 'r', encoding='utf8') as f:
    movie = json.load(f)


for m in movie:
    A = []
    mactor = m['fields']['genres']
    if mactor != [""]:
        for mc in mactor:
            A.append(gpk[mc])
            m['fields']['genres'] = A


with open('KMDB_Moviefinal.json', 'w', encoding="utf-8") as make_file:
    json.dump(movie, make_file, ensure_ascii=False, indent="\t")