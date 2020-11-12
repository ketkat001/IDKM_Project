# -*- coding: utf-8 -*-
import requests
import json
from collections import OrderedDict
from bs4 import BeautifulSoup
from pprint import pprint

genresd = {
    28: "액션",
    12: "모험",
    16: "애니메이션",
    35: "코미디",
    80: "범죄",
    99: "다큐멘터리",
    18: "드라마",
    10751: "가족",
    14: "판타지",
    36: "역사",
    27: "공포",
    10402: "음악",
    9648: "미스터리",
    10749: "로맨스",
    878: "SF",
    10770: "TV 영화",
    53: "스릴러",
    10752: "전쟁",
    37: "서부"
    }



A = []
ACT = []
for sc in range(1, 501):
    print(sc)
    url = f"https://api.themoviedb.org/3/movie/top_rated?api_key=9bd3393b06f6e8bd8002317b32184318&language=ko-KR&page={sc}"
    rdata = requests.get(url)
    st_json = json.loads(rdata.text)
    # data = json.load(rdata)
    for st in st_json['results']:
        A1 = OrderedDict()
        A1['model'] = "movies.movie"
        A1['pk'] = st['id']
        A1['fields'] = OrderedDict()
        A1['fields']['title'] = st['title']
        A1['fields']['poster_url'] = st['poster_path']
        A1['fields']['overview'] = st['overview']
        A1['fields']['rating'] = st['adult']
        A1['fields']['release_date'] = st['release_date']
        gl = ''
        for g in st['genre_ids']:
            gl += genresd[int(g)] + ', '
        A1['fields']['genres'] = gl[:-2]
        mvid = st['id']
        url_ac = f'https://api.themoviedb.org/3/movie/{mvid}/credits?api_key=9bd3393b06f6e8bd8002317b32184318&language=ko-KR'
        acdata = requests.get(url_ac)
        ac_json = json.loads(acdata.text)
        # print(ac_json)
        anum = 0
        act_l = []
        for actor in ac_json['cast']:
            if anum >= 5:
                break
            else:
                act_od = OrderedDict()
                act_od['model'] = 'movies.actor'
                act_od['pk'] = actor['id']
                act_od['fields'] = OrderedDict()
                act_od['fields']['actor_id'] = actor['id']
                act_od['fields']['name'] = actor['name']
                act_od['fields']['profile_path'] = actor['profile_path']
                act_l.append(int(actor['id']))
                anum += 1
            ACT.append(act_od)
        A1['fields']['actors'] = act_l       
        A.append(A1)


with open('TMDB_movie.json', 'w', encoding="utf-8") as make_file:
    json.dump(A, make_file, ensure_ascii=False, indent="\t")


with open('TMDB_actor.json', 'w', encoding="utf-8") as make_file:
    json.dump(ACT, make_file, ensure_ascii=False, indent="\t")

