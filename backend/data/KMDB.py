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
with open('KMDB_movie.json', 'w', encoding="utf-8") as make_file:
    while startCount < 1:
        # url = f"http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json2.jsp?collection=kmdb_new2&listCount=500&title={title}&detail=Y&ServiceKey=H4T135AW903C3067983L"
        url = f"http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json2.jsp?collection=kmdb_new2&listCount=500&startCount={startCount}&detail=Y&ServiceKey=H4T135AW903C3067983L"
        request = ul.Request(url)
        # print(request)
        response = ul.urlopen(request)
        rescode = response.getcode()
        file_data = OrderedDict()
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
            actors = []
            len_act = 3 
            if len(data['actors']['actor']) > 3:
                len_act = 3
            else:
                len_act = len(data['actors']['actor'])
            for i in range(len_act):
                actor = data['actors']['actor'][i]['actorNm']
                actors.append(actor)
            nation = data['nation']
            maker = data['company']
            plot_kr = data['plots']['plot'][0]['plotText']
            # plot_en = movieData[0]['Result'][0]['plots']['plot'][1]['plotText']
            runtime = data['runtime']
            ratingGrade = data['rating']
            genre = data['genre']
            repRlsDate = data['repRlsDate']
            keywords = data['keywords']
            posters = data['posters'] #수정 필요 이미지 두개가 붙어있음
            file_data['model'] = "movies.movie"
            file_data['pk'] = data['DOCID']
            file_data['fields'] = {"title": title, "director": director, "actors": actors, "nation":nation, "maker": maker, "plot_kr": plot_kr, "runtime": runtime, "ratingGrade": ratingGrade, "genre": genre, "repRlsDate": repRlsDate, "keywords": keywords}
            json.dump(file_data, make_file, ensure_ascii=False, indent="\t")

        startCount += 500

