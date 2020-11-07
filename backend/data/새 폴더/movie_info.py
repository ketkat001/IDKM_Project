# -*- coding: utf-8 -*-
import urllib.request as ul
import json
from collections import OrderedDict

movieCd = "04629"
url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key=430156241533f1d058c603178cc3ca0e&movieCd={20182530}"
request = ul.Request(url)

response = ul.urlopen(request)
rescode = response.getcode()
file_data = OrderedDict()
# file_data[name] = {}

if(rescode == 200):
	responseData = response.read()

result = json.loads(responseData)
movieInfoResult = result['movieInfoResult']
movieInfo = movieInfoResult['movieInfo']
print(movieInfo)
# with open('movie2018.json', 'w', encoding="utf-8") as make_file:
#     for movie in movieList:
#         file_data['model'] = "movies.movie"
#         # print(movie)
#         file_data['pk'] = movie['movieCd']
#         file_data['fields'] = {"movieNm": movie['movieNm'], "movieNmEn": movie['movieNmEn'], "openDt": movie['openDt'], "repGenreNm": movie['repGenreNm']}
#         json.dump(file_data, make_file, ensure_ascii=False, indent="\t")


# # movieNm = movieList['movieNm']

# # print(result)
