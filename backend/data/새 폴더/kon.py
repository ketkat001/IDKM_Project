from konlpy.utils import pprint
from konlpy.tag import Hannanum
import requests
import json
import urllib.request as ul
import urllib
from collections import OrderedDict
from konlpy.tag import Kkma


kkma = Kkma()
# hannanum = Hannanum()
startCount = 0
A = []
words = []
with open('KMDB_movie.json', 'w', encoding="utf-8") as make_file:
    while startCount < 500:
        url = f"http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json2.jsp?collection=kmdb_new2&listCount=500&startCount={startCount}&detail=Y&ServiceKey=H4T135AW903C3067983L"
        request = ul.Request(url)
        response = ul.urlopen(request)
        rescode = response.getcode()
        
        if(rescode == 200):
            responseData = response.read()

        result = json.loads(responseData)
        movieData = result['Data']
        datas = movieData[0]['Result']
        for data in datas:
            file_data = OrderedDict()
            plot_kr = data['plots']['plot'][0]['plotText']
            keywords = data['keywords']
            words= kkma.nouns(plot_kr)
            # word= kkma.sentences(words)
            # words.append(hannanum.morphs(plot_kr))
            # pprint(hannanum.morphs(plot_kr))
            file_data['words'] = words
            file_data['keywords'] = data['keywords']
            A.append(file_data)
            # file_data['fields'] = {"title": title, "director": director, "actors": actors, "nation":nation, "maker": maker, "plot_kr": plot_kr, "runtime": runtime, "ratingGrade": ratingGrade, "genre": genre, "repRlsDate": repRlsDate, "keywords": keywords}
        startCount += 500
    json.dump(A, make_file, ensure_ascii=False, indent="\t")