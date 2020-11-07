from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

# 크롤링한 결과 저장할 df 만들어놓기
df = pd.DataFrame(columns=["title", "genre", "year", "netflix"])
count = 0

# 크롤링
for num in range(1,4451):
    url = "https://www.4flix.co.kr/board/netflix/" + str(num)
    with urllib.request.urlopen(url) as url:
        try:
            doc = url.read()
            soup = BeautifulSoup(doc, "html.parser")
            # print(soup)
            title_year = soup.find_all("h1")[2].text.strip() # 제목(연도) 
            # print('--')
            # logo = soup.find_all("h1")[1].text.strip() # 제목(연도) 
            # print(logo)
            # logo_link = logo.find('a')['href']
            # print(logo_link)
            title = title_year[:-6] #제목만
            year = title_year[-5:-1] #연도만
            genre = soup.find_all("h3")[1].text.strip()
            netflix = soup.find_all("p")[0].text.strip()
            link = soup.find_all("a")[41]['href']
            print(link)
        
            df.loc[count] = [title, genre, year, netflix]
            count+=1
        except:
            pass #3039는 글 지워짐 
# df.to_csv('movie_project.csv', index=False, encoding='utf-8')

