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
number = 5
with open('KMDB_movie.json', 'w', encoding="utf-8") as make_file:
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
            print(data)
            break
            file_data = OrderedDict()
            print(len(data['actors']['actor']))
            director = data['directors']['director'][0]['directorNm']
            title = data['title']
            actors = ''
            genres = ''
            tagdatas = ''
            len_act = 1 
            if len(data['actors']['actor']) >1:
                len_act = len(data['actors']['actor'])
            else:
                len_act = 0
            for i in range(len_act):
                actors = actors +  str(data['actors']['actor'][i]['actorNm'])
                if i == len_act - 1:
                    pass
                else:
                    actors = actors + ','
            tagdatas += actors + ','
            nation = data['nation']
            maker = data['company']
            overview = data['plots']['plot'][0]['plotText']
            # plot_en = movieData[0]['Result'][0]['plots']['plot'][1]['plotText']
            # print(data['actors'])
            tagdatas += overview + ' '
            if data['runtime']:
                runningtime = int(data['runtime'])
            else:
                runningtime = 0
            if data['rating']:
                rating = data['rating']
            else:
                rating = "0"
            if data['repRlsDate']:
                release_date = int(data['repRlsDate'])
            else:
                release_date = 0
            genres = str(data['genre'])
 
            k = data['genre']

            a = list(map(str, k.split(',')))

            for i in range(len(a)):
                tagdatas += a[i] + ', '

            # for i in range(genre):
            #     genres.append(genre[i])

            # overview_tags = data['keywords']
            # if data['posters']:

            #     poster_url = ''.join(data['posters']).split('|')  #수정 필요 이미지 두개가 붙어있음
            # else:
            #     poster_url = ''

  
            file_data['model'] = "movies.movie"
            file_data['pk'] = str(number)
            number += 1
            file_data['fields'] = {"title": title, "poster_url": data['posters'], "director": director, "actors": actors, "genres": genres, "nation": nation, "maker": maker, "overview": overview, "runningtime": runningtime, "rating": rating, "release_date": release_date, "tagdatas": tagdatas}
            A.append(file_data)
        startCount += 500
    json.dump(A, make_file, ensure_ascii=False, indent="\t")


