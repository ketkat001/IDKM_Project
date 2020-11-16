# 영화 추천 서비스

## How to use

Frontend 
```
# move to forntend folder
npm install 
npm run serve
```

Backend
```
# move to backend folder
# 가상 환경을 켜줍니다.
$ python -m venv venv
$ source venv/Scripts/activate
# $ source venv/bin/activate <= for linux
# 필요한 설치파일을 다운 받습니다.
$ pip install -r requirements.txt
$ pip install sklearn pymysql

# 모델링 데이터 베이스에 등록
$ python manage.py makemigrations
$ python manage.py migrate
# 문화재 데이터를 등록합니다.
$ python manage.py loaddata genres.json KMDB_actor_name_1.json TMDB_overtags.json TMDB_Moviefinal.json
# 백엔드 실행
$ python manage.py runserver
```

## Usage

### 자연어 처리를 통한 강력한 영화 검색 기능

* 이제 문장으로 검색해보세요!

* 제목이나 배우의 이름이 생각나지 않더라도 괜찮아요!

## Structure

```bash
s03p31a504
├─backend
│  ├─accounts
│  ├─backend
│  ├─data
│  ├─movies
│  └─venv
│
└─frontend
    ├─node_modules
    ├─public
    └─src
        ├─api
        ├─assets
        │  ├─css
        │  └─img
        ├─components
        ├─plugins
        ├─views
        └─vuex
```




## About Us

### 팀장 
최정원

### 팀원
강용준

김보성

김진혁
Git: https://github.com/rexiann/

나종석

