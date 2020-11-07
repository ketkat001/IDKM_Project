# -*- coding: utf-8 -*-
import urllib.request as ul
import json
from collections import OrderedDict


flag = 0
with open('movie_list.json', 'w', encoding="utf-8") as make_file:
    curPage = 1
    while flag < 100:
        openStartDt = "1900"
        int(openStartDt)
        # movieTypeCd	= ''
        openEndDt = 2020
        itemPerPage = "100"
        int(itemPerPage)
        url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=430156241533f1d058c603178cc3ca0e&openStartDt={openStartDt}&curPage={curPage}&itemPerPage={itemPerPage}"
        request = ul.Request(url)

        response = ul.urlopen(request)
        rescode = response.getcode()
        file_data = OrderedDict()
        # file_data[name] = {}

        if(rescode == 200):
            responseData = response.read()

        result = json.loads(responseData)
        print(result)
        movieListResult = result['movieListResult']
        movieList = movieListResult['movieList']
        for movie in movieList:
            file_data['model'] = "movies.movie"
            # print(movie)
            file_data['pk'] = movie['movieCd']
            file_data['pk'] = movie['movieCd']
            file_data['fields'] = {"movieNm": movie['movieNm'], "movieNmEn": movie['movieNmEn'], "openDt": movie['openDt'], "repGenreNm": movie['repGenreNm']}
            json.dump(file_data, make_file, ensure_ascii=False, indent="\t")


        curPage += 1
        print(curPage)
        flag += 1
    # movieNm = movieList['movieNm']

    # print(result)
