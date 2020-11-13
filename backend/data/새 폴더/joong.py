import json
from collections import OrderedDict

with open('TMDB_actor.json', 'r', encoding='utf8') as f:
    movie = json.load(f)
nm = []
nm2 = []
for m in movie:
    if m['pk'] not in nm2:
        nm.append(m)
        nm2.append(m['pk'])


with open('TMDB_actor2.json', 'w', encoding="utf-8") as make_file:
    json.dump(nm, make_file, ensure_ascii=False, indent="\t")