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
cast = []
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
        

        number = 1
        for data in datas:
            file_data = OrderedDict()
            number = []
            # print(len(data['actors']['actor']))
            director = data['directors']['director'][0]['directorNm']
            title = data['title']
            actors = []
            len_act = len(data['actors']['actor'])
            for k in range(len_act):
                name = data['actors']['actor'][k]['actorNm']
                # print(name, 'before')
                if name not in actors and name != "":
                    # print(name, 'after')
                    actors.append(name)
                    cast.append(name, len(actors))
                    number.append(len(actors))
                else:
                    num = 
            nation = data['nation']
            maker = data['company']
            overview = data['plots']['plot'][0]['plotText']
            # plot_en = movieData[0]['Result'][0]['plots']['plot'][1]['plotText']
            runningtime = data['runtime']
            ratingGrade = data['rating']
            genre = data['genre']
            release_date = data['repRlsDate']
            overview_tags = data['keywords']
            posters = data['posters'] #수정 필요 이미지 두개가 붙어있음
            file_data['model'] = "movies.movie"
            file_data['pk'] = number
            number += 1
            file_data['fields'] = {"title": title, "director": director, "actors": cast, "nation": nation, "maker": maker, "overview": overview, "runningtime": runningtime, "ratingGrade": ratingGrade, "genre": genre, "release_date": release_date, "overview_tags": overview_tags}
            A.append(file_data)
        json.dump(A, make_file, ensure_ascii=False, indent="\t")

        startCount += 1