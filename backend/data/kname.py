import json
import requests
from bs4 import BeautifulSoup
from collections import OrderedDict

with open('TMDB_actor2.json', 'r', encoding='utf8') as f:
    actor_j = json.load(f)

act_json = OrderedDict()
for at in actor_j:
    aname = at['fields']['name']
    aaname = aname.replace(' ', '+')
    print(aaname)
    url = f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={aaname}'
    rdata = requests.get(url)
    soup = BeautifulSoup(rdata.text, 'html.parser')
    A = soup.select('#people_info_z > div > div.api_cs_wrap > div.cont_noline > div > dl > dd.name > a > strong')
    if A != []:
        at['fields']['k_name'] = A

    else:
        url2 = f'https://www.google.com/search?q={aaname}&oq={aaname}&aqs=chrome..69i57j0i19l7.315j0j9&sourceid=chrome&ie=UTF-8'
        rdata2 = requests.get(url2)
        soup2 = BeautifulSoup(rdata2.text, 'html.parser')
        AA = soup2.findAll("div", {"class": "BNeawe deIvCb AP7Wnd"})
        AAA = str(AA)[35:]
        AAAA = AAA.split(' (')
        at['fields']['k_name'] = AAAA[0]


with open('TMDB_actor3.json', 'w', encoding="utf-8") as make_file:
    json.dump(actor_j, make_file, ensure_ascii=False, indent="\t")