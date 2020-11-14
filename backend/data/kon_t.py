from konlpy.utils import pprint
import json
import urllib.request as ul
import urllib
from collections import OrderedDict
from konlpy.tag import Kkma


kkma = Kkma()
allovert = []


with open('TMDB_movie.json', 'r', encoding='utf8') as f:
    movie = json.load(f)

with open('KMDB_actor_name_1.json', 'r', encoding='utf8') as f:
    actor_j = json.load(f)

act_json = OrderedDict()
for act1 in actor_j:
    act_json[act1['pk']] = act1['fields']['ko_name']#k_name으로 수정해야함

alltags = []
nnn = 0
for m in movie:
    A = []
    tdata = m['fields']['overview'] + ' ' + m['fields']['genres']
    actor_l = m['fields']['actors']
    
    actor_l2 = []
    for act in actor_l:
        if act in act_json.keys():
            actor_l2.append(act)
            tdata += ', ' + act_json[act]
    m['fields']['actors'] = actor_l2
    words= kkma.nouns(tdata)
    m['fields']['tagdatas'] = words
    alltags.extend(words)
    nnn += 1
    
tntn = {}

for tn_tag in alltags:
    if tn_tag not in tntn:
        tntn[tn_tag] = 1
    else:
        tntn[tn_tag] += 1
alltags2 = []
for k, v in tntn.items():
    if v >= 2 and len(k) >= 2:
        alltags2.append(k)


# print(len(alltags))
# alltags = set(alltags)
# print(len(alltags))
# alltags = list(alltags)
# print(alltags)
num = 1
for at in alltags2:
    overt = OrderedDict()
    overt['model'] = 'movies.tagdatas'
    overt['pk'] = num
    overt['fields'] = OrderedDict()
    overt['fields']['tags'] = at
    allovert.append(overt)
    num += 1

with open('TMDB_Moviefinal.json', 'w', encoding="utf-8") as make_file:
    json.dump(movie, make_file, ensure_ascii=False, indent="\t")

#중복되는 키워드 제거하기
with open('TMDB_overtags.json', 'w', encoding="utf-8") as make_file:
    json.dump(allovert, make_file, ensure_ascii=False, indent="\t")
