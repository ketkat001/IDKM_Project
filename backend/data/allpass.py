# -*- coding: utf-8 -*-
import requests
import json
import urllib.request as ul
import urllib
from collections import OrderedDict
from konlpy.utils import pprint
from konlpy.tag import Hannanum
from konlpy.tag import Kkma

with open('KMDB_overtags.json', 'r', encoding='utf8') as f:
    ovt = json.load(f)


with open('KMDB_Moviefinal.json', 'r', encoding='utf8') as f:
    movie = json.load(f)

A1 = OrderedDict()

for o in ovt:
    tagnanme = o['fields']['tags']
    pkn = o['pk']
    A1[tagnanme] = pkn

for m in movie:
    if m['fields']['tagdatas'] == [""]:
        m['fields']['tagdatas'] = []


    # A = []
    # mactor = m['fields']['tagdatas']
    # if mactor != [""]:
    #     for mc in mactor:
    #         A.append(A1[mc])
    #         m['fields']['tagdatas'] = A
    # else:
    #     m['fields']['tagdatas'] = []

with open('KMDB_Moviefinal.json', 'w', encoding="utf-8") as make_file:
    json.dump(movie, make_file, ensure_ascii=False, indent="\t")
    
# #actor 변경 (준비물 KMDB_actor_pk, KMDB_movie)
# with open('KMDB_actor_pk.json', 'r', encoding='utf8') as f:
#     actorpk = json.load(f)

# with open('KMDB_movie.json', 'r', encoding='utf8') as f:
#     movie = json.load(f)


# for m in movie:
#     A = []
#     mactor = m['fields']['actors']
#     if mactor != [""]:
#         for mc in mactor:
#             A.append(actorpk[mc])
#             m['fields']['actors'] = A

# #장르변경 준비물(KMDB_genre_pk)
# with open('KMDB_genre_pk.json', 'r', encoding='utf8') as f:
#     gpk = json.load(f)

# for m in movie:
#     A = []
#     mactor = m['fields']['genres']
#     if mactor != [""]:
#         for mc in mactor:
#             A.append(gpk[mc])
#             m['fields']['genres'] = A
#     else:
#         m['fields']['genres'] = []

# #overview 변경 준비물(KMDB_over_j_pk)
# kkma = Kkma()
# allovert = []
# alltags = []
# for m in movie:
#     A = []
#     overview = m['fields']['overview']
#     words= kkma.nouns(overview)
#     alltags.extend(words)
#     m['fields']['overview_tags'] = words


# with open('KMDB_over_j_pk.json', 'r', encoding='utf8') as f:
#     gpk = json.load(f)

# for m in movie:
#     A = []
#     mactor = m['fields']['overview_tags']
#     if mactor != [""]:
#         for mc in mactor:
#             A.append(gpk[mc])
#             m['fields']['overview_tags'] = A




