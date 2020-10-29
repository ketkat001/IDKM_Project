#제목: 네이버 검색 API 활용하기
import urllib.request


#애플리케이션 클라이언트 id 및 secret
x = ''
client_id = "dZH1aciTrgSCttKYJwm7"
client_secret = "TTsxwsewLU"
url = "https://openapi.naver.com/v1/search/movie.json"
option = "&display=100&sort=count&"
query = "?query="+urllib.parse.quote("캐리비안의")
url_query = url + query + option

request = urllib.request.Request(url_query)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

#검색 요청 및 처리
response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode == 200):
 
    response_body = response.read()
 
    print(response_body.decode('utf-8'))
 
else:
 
    print("Error code:"+rescode)