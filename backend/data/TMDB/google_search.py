import random
import requests
from bs4 import BeautifulSoup 
import json
from collections import OrderedDict
import traceback
import ssl, urllib, sys, os
from pprint import pprint
import traceback
import time

A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
       )
 
Agent = A[random.randrange(len(A))]
headers = {'user-agent': Agent}
hdr = {'user-agent': 'Mozilla/5.0'}
with open('KMDB_movie.json', 'r', encoding='utf8') as f:
    movies = json.load(f)
actor_lst = []
number = 0
# https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=Jason+Statham
for movie in movies:
    try:
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' +movie['name']
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        target = str(soup.select('#people_info_z > div > div.api_cs_wrap > div.cont_noline > div > dl > dd.name > a > strong'))

        if len(target) != 2:
            movie['ko_name'] = target[9:-10]
            actor_lst.append(movie)
            
        else:
            a = movie['name']
            hdr = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
            url = f'https://www.google.com/search?q={a}'
            time.sleep(0.5)
            r = requests.get(url, headers=hdr)
            soup = BeautifulSoup(r.text, 'lxml')
            try:
                targets = soup.find("div", { "class": "SPZz6b"})
                target = targets.find("span")
                if target.text == '이것을 찾으셨나요?':
                    pass
                else:

                    movie['ko_name'] = target.text
                    actor_lst.append(movie)
                    time.sleep(0.5)
                    print(target.text)
            except:
                print(movie['name'], ' except걸린놈')
                time.sleep(0.5)
                pass
        print(number)
        number += 1
    except:
        number +=1
        print(number, 'except')


with open('KMDB_actor_name_final.json', 'w', encoding="utf-8") as make_file:
    json.dump(actor_lst, make_file, ensure_ascii=False, indent="\t")