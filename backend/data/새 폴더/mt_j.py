# -*- coding: utf-8 -*-
import requests
import json
import urllib.request as ul
import urllib
from collections import OrderedDict



# with open('KMDB_overtags.json', 'r', encoding='utf8') as f:
#     json_data = json.load(f)
# A = OrderedDict()

# for j in json_data:
#     pk = j['pk']
#     name = j['fields']['tags']
#     A[name] = str(pk)
# with open('KMDB_over_j_pk.json', 'w', encoding="utf-8") as make_file:
#     json.dump(A, make_file, ensure_ascii=False, indent="\t")



with open('KMDB_over_j_pk.json', 'r', encoding='utf8') as f:
    gpk = json.load(f)

with open('KMDB_Moviefinal.json', 'r', encoding='utf8') as f:
    movie = json.load(f)


for m in movie:
    A = []
    mactor = m['fields']['overview_tags']
    if mactor != [""]:
        print(mactor)
        for mc in mactor:
            A.append(gpk[mc])
            m['fields']['overview_tags'] = A


with open('KMDB_Moviefinal.json', 'w', encoding="utf-8") as make_file:
    json.dump(movie, make_file, ensure_ascii=False, indent="\t")