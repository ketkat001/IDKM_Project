# -*- coding: utf-8 -*-
import requests
import json
import urllib.request as ul
import urllib
from collections import OrderedDict


# title = "극한직업"
# title = urllib.parse.quote(title)
# print(type(title))
startCount = 0
A = []
number = 1
api_key = '560c0e0b21628cdf0431b39687354675'
person_id = 1
with open('KMDB_movie.json', 'w', encoding="utf-8") as make_file:
    while person_id < 1000000:
     
        # url = f"http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json2.jsp?collection=kmdb_new2&listCount=500&title={title}&detail=Y&ServiceKey=H4T135AW903C3067983L"
        url = f"https://api.themoviedb.org/3/person/{person_id}?api_key={api_key}&language=ko-kr"

        request = ul.Request(url)
        # print(request)
        try:
            response = ul.urlopen(request)
            rescode = response.getcode()
        # file_data[name] = {}

            if(rescode == 200):
                responseData = response.read()

            result = json.loads(responseData)
            actordata = {'name': result['name'],
                        'also_known_as': result['also_known_as'],
                        'profile_path': result['profile_path']}
        except:
            person_id += 1
            continue
        print(actordata)


        person_id += 1
    json.dump(A, make_file, ensure_ascii=False, indent="\t")


