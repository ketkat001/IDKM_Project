from bs4 import BeautifulSoup
import urllib.request




# 크롤링

url = "https://watcha.com/home"
url = urllib.request.urlopen(url)
doc = url.read()
soup = BeautifulSoup(doc, "html.parser")
# print(soup)
# title = soup.select('.css-iggh3a-Text el11hez1')
# title = soup.find('div', {"class"="css-iggh3a-Text el11hez1"})
# print(title)
# df.to_csv('movie_project.csv', index=False, encoding='utf-8')
a = soup.find_all("section")
b = soup.find_all("section")
c = soup.find_all("section")
d = soup.find_all("section")
print(title)

