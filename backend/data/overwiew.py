# -*- coding: utf-8 -*-
import requests
import json
import urllib.request as ul
import urllib
from collections import OrderedDict
from konlpy.utils import pprint
from konlpy.tag import Kkma

# title = "극한직업"
# title = urllib.parse.quote(title)
# print(type(title))
startCount = 0
kkma = Kkma()
i = 0
A = []
word_list = []
with open('KMDB_over.json', 'w', encoding="utf-8") as make_file:
    while startCount < 1:
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
            plot_kr = data['plots']['plot'][0]['plotText']
            keywords = data['keywords']
            words= kkma.nouns(plot_kr)
            print(words)
            for word in words:    
                if word not in word_list:
                    file_data = OrderedDict()
                    word_list.append(word)
                    file_data['model'] = "movies.movie_cast"
                    file_data['pk'] = len(word_list)
                    file_data['fields'] = {"word": word}
                    A.append(file_data)

        startCount += 500

    json.dump(A, make_file, ensure_ascii=False, indent="\t")