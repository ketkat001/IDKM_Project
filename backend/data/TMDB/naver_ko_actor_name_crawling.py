import requests
from bs4 import BeautifulSoup 
import json
from collections import OrderedDict
import traceback
import ssl, urllib
from pprint import pprint

base_url = 'https://www.google.co.kr/search'

with open('KMDB_movie.json', 'r', encoding='utf8') as f:
    movies = json.load(f)
    
for movie in movies:
    print(movie['name'])


    values = {
        'q': movie['name'] + ' 나무위키',
        'oq': movie['name'] + ' 나무위키',
        'aqs': 'chrome..69i57.35694j0j7',
        'sourceid': 'chrome',
        'ie': 'UTF-8',
    }
    f'https://www.google.com/search?q={movie['name']}&oq={movie['name']}&aqs=chrome..69i57j69i59l2j0i30l2j69i60l3.170j0j7&sourceid=chrome&ie=UTF-8'
    hdr = {'User-Agent': 'Mozilla/5.0'}
    query_string = urllib.parse.urlencode(values)
    req = urllib.request.Request(base_url + '?' + query_string, headers=hdr)
    print(req)
    context = ssl._create_unverified_context()
    try:
        res = urllib.request.urlopen(req, context=context)
    except:
        traceback.print_exc()

    print(context)



    html_data = BS(res.read(), 'html.parser')
    
    break
    g_list = html_data.find_all('div', attrs= {'class': 'ellip'})
    print(g_list)
    break
    try:
        for g in g_list:
            ahref = g.find('a')['href']
            ahref = 'https://www.google.co.kr' + ahref
            # 컨텐츠에서 검색결과와 일치하는 부분 꺼내기 
            span = g.find('span', attrs={'class': 'st'})
            if span:
                span_text = span.get_text()
                span_text = span_text.replace(' ', '')
                span_text = span_text.replace('\n', '')
    except:
        traceback.print_exc()

