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
genre_list = []
with open('KMDB_genre.json', 'w', encoding="utf-8") as make_file:
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
            file_data = OrderedDict()
            genres = data['genre'].split(',')
            print(genres)
            for genre in genres:  
                if genre not in genre_list and genre != "":
                        file_data = OrderedDict()
                        # print(name, 'after')
                        genre_list.append(genre)
                        file_data['model'] = "movies.genre"
                        file_data['pk'] = len(genre_list)
                        file_data['fields'] = {"name": genre}
                        A.append(file_data)
    
        startCount += 500
    json.dump(A, make_file, ensure_ascii=False, indent="\t")

