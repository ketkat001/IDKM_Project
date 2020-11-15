# 데이터 불러오기
from numpy.linalg import norm
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pymysql


def recommend_sys(searchword):
    df = DataFrame()
    movie_db = pymysql.connect(
        user='root',
        passwd='ssafy',
        host='127.0.0.1',
        db='DKM',
        charset='utf8'
    )

    cursor = movie_db.cursor(pymysql.cursors.DictCursor)

    sql = "select * from movies_movie;"
    cursor.execute(sql)
    result = cursor.fetchall()
    result = pd.DataFrame(result)

    resultA = [searchword]
    resultA.extend(list(result['searchdata'].values))
    tfidf_vect_simple = TfidfVectorizer()
    feature_vect_simple = tfidf_vect_simple.fit_transform(resultA)

    resultAname = [1]
    resultAname.extend(list(result['id'].values))

    similarity_simple_pair = cosine_similarity(
        feature_vect_simple[0], feature_vect_simple)

    movie_lank = pd.DataFrame(
        {'id': resultAname, 'score': similarity_simple_pair[0]})
    df1 = movie_lank.sort_values(by=['score'], ascending=False)
    df1 = df1[1:11]
    df2 = list(df1['id'].values)

    return df2


def recommend_sys2(user_pk):
    df = DataFrame()
    movie_db = pymysql.connect(
        user='root',
        passwd='ssafy',
        host='127.0.0.1',
        db='DKM',
        charset='utf8'
    )

    cursor = movie_db.cursor(pymysql.cursors.DictCursor)

    sql = "select * from movies_movie;"
    cursor.execute(sql)
    result = cursor.fetchall()
    result = pd.DataFrame(result)

    sql3 = "select * from movies_tagdatas;"
    cursor.execute(sql3)
    result3 = cursor.fetchall()
    result3 = pd.DataFrame(result3)

    sql = f"select * from movies_user_tagdatas where user_id={user_pk};"
    cursor.execute(sql)
    result2 = cursor.fetchall()
    result2 = pd.DataFrame(result2)

    result2 = result2.sort_values(by=['weight'], ascending=False)
    result2 = result2[0:20]
    result2A = list(result2['tagdata_id'].values)

    searchword = []
    for r2a in result2A:
        searchword.append(result3[result3['id'] == r2a]['tags'].values[0])
    searchword2 = ' '.join(searchword)
    resultA = [searchword2]

    resultA.extend(list(result['searchdata'].values))
    tfidf_vect_simple = TfidfVectorizer()
    feature_vect_simple = tfidf_vect_simple.fit_transform(resultA)

    resultAname = [1]
    resultAname.extend(list(result['id'].values))

    similarity_simple_pair = cosine_similarity(
        feature_vect_simple[0], feature_vect_simple)

    sql = f"select * from movies_movie_user_watched where user_id={user_pk};"
    cursor.execute(sql)
    result5 = cursor.fetchall()
    result5 = pd.DataFrame(result5)

    QQ = list(result5['movie_id'].values)

    movie_lank = pd.DataFrame(
        {'id': resultAname, 'score': similarity_simple_pair[0]})
    df1 = movie_lank.sort_values(by=['score'], ascending=False)
    df1 = list(df1['id'].values)
    df2 = []
    num = 0
    for ddd in df1:
        if num == 10:
            break
        if ddd not in QQ:
            df2.append(ddd)
            num += 1

    return df2
