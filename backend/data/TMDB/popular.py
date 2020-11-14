# -*- coding: utf-8 -*-
import requests
import json
import urllib.request as ul
import urllib
from collections import OrderedDict
from pprint import pprint


# title = "극한직업"
# title = urllib.parse.quote(title)
# print(type(title))
startCount = 0
A = []
number = 1
api_key = '560c0e0b21628cdf0431b39687354675'
with open('KMDB_movie.json', 'w', encoding="utf-8") as make_file:
    while number < 1000:

        try:
            print(number)
            url = f"https://api.themoviedb.org/3/person/popular?api_key={api_key}&language=ko-kr&page={number}"
            request = ul.Request(url)
            response = ul.urlopen(request)
            rescode = response.getcode()
            responseData = response.read()
            result = json.loads(responseData)
            actordata = []
            for i in range(20):
                actordata = {'name': result['results'][i]['name'],
                'actor_id': result['results'][i]['id'],
                'profile_path': result['results'][i]['profile_path']}
                A.append(actordata)
                actordata = []
            number += 1

        # try:
        #     response = ul.urlopen(request)
        #     rescode = response.getcode()
        # # file_data[name] = {}

        #     if(rescode == 200):
        #         responseData = response.read()

        #     result = json.loads(responseData)
        #     actordata = {'name': result['name'],
        #                 'also_known_as': result['also_known_as'],
        #                 'profile_path': result['profile_path']}
        # except:
        #     number += 1
        #     continue
        # print(actordata['page'])
        except:
            
            number += 1
            print(number)
    print(A)
    json.dump(A, make_file, ensure_ascii=False, indent="\t")


