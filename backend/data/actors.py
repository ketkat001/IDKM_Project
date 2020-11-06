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
i = 0
A = []
actors = []
with open('KMDB_actors.json', 'w', encoding="utf-8") as make_file:
    while startCount < 1000:
        # url = f"http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json2.jsp?collection=kmdb_new2&listCount=500&title={title}&detail=Y&ServiceKey=H4T135AW903C3067983L"
        url = f"http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json2.jsp?collection=kmdb_new2&listCount=500&startCount={startCount}&detail=Y&ServiceKey=H4T135AW903C3067983L"
        request = ul.Request(url)
        # print(request)
        response = ul.urlopen(request)
        rescode = response.getcode()
        
        # file_data[name] = {}

        if(rescode == 200):
            responseData = response.read()

        result = json.loads(responseData)
        # print(result)
        movieData = result['Data']
        datas = movieData[0]['Result']
        for data in datas:
            
            # print(len(data['actors']['actor']))
            director = data['directors']['director'][0]['directorNm']
            title = data['title']
            
            len_act = len(data['actors']['actor'])
            # if len(data['actors']['actor']) > 3:
            #     len_act = data['actors']['actor']
            # else:
            #     len_act = len(data['actors']['actor'])
            for k in range(len_act):
                
                name = data['actors']['actor'][k]['actorNm']
                # print(name, 'before')
                if name not in actors and name != "":
                    file_data = OrderedDict()
                    # print(name, 'after')
                    actors.append(name)
                    file_data['model'] = "movies.movie_cast"
                    file_data['pk'] = len(actors)
                    file_data['fields'] = {"movie_actors": name}
                    A.append(file_data)

        startCount += 500

    json.dump(A, make_file, ensure_ascii=False, indent="\t")