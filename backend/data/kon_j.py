from konlpy.utils import pprint
import json
import urllib.request as ul
import urllib
from collections import OrderedDict
from konlpy.tag import Kkma


kkma = Kkma()
allovert = []


with open('KMDB_movie.json', 'r', encoding='utf8') as f:
    movie = json.load(f)
alltags = []

for m in movie:
    A = []
    overview = m['fields']['tagdatas']
    words= kkma.nouns(overview)
    actor_l = list(m['fields']['actors'].split(','))
    alltags.extend(actor_l)
    for act in actor_l:
        words.append(act)
    m['fields']['tagdatas'] = words
    alltags.extend(words)
    

num = 1
for at in alltags:
    overt = OrderedDict()
    overt['model'] = 'movies.tagdatas'
    overt['pk'] = num
    overt['fields'] = OrderedDict()
    overt['fields']['tags'] = at
    allovert.append(overt)
    num += 1

with open('KMDB_Moviefinal.json', 'w', encoding="utf-8") as make_file:
    json.dump(movie, make_file, ensure_ascii=False, indent="\t")

#중복되는 키워드 제거하기
with open('KMDB_overtags.json', 'w', encoding="utf-8") as make_file:
    json.dump(allovert, make_file, ensure_ascii=False, indent="\t")
