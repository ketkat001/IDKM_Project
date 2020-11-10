import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import pymysql
from konlpy.tag import Kkma


def recommend_sys(searchword):
    kkma = Kkma()
    df = DataFrame()
    movie_db = pymysql.connect(
        user='root', 
        passwd='ssafy', 
        host='127.0.0.1', 
        db='DKM', 
        charset='utf8'
    )

    cursor = movie_db.cursor(pymysql.cursors.DictCursor)

    sql = "select * from movies_tagdatas;"
    cursor.execute(sql)
    result = cursor.fetchall()
    result = pd.DataFrame(result)

    sql2 = "select * from movies_movie;"
    cursor.execute(sql2)
    result2 = cursor.fetchall()
    result2 = pd.DataFrame(result2)

    sql3 = "select * from movies_movie_tagdatas;"
    cursor.execute(sql3)
    result3 = cursor.fetchall()
    result3 = pd.DataFrame(result3)

    result3['weight'] = 1

    mydict = pd.DataFrame()
    D = pd.DataFrame(mydict)

    words= kkma.nouns(searchword)

    for w in words:
        words_s = result[result['tags'] == w]
        D = pd.concat([D, words_s], ignore_index=True)
    if len(D) == 0:
        return []
    else:
        D = D.drop('tags', axis=1)
        D.columns = ['tagdatas_id']
        D['movie_id'] = 1
        D['weight'] = 1

        result3 = pd.concat([result3, D], ignore_index=True)

        data_df1 = result3.pivot_table(index='movie_id', columns='tagdatas_id', values = 'weight')
        data_df1.fillna(0, inplace=True)
        # print(data_df1)
        m1 = Series(data_df1.loc[1])

        # print(m1)
        data_df2 = data_df1.mul(m1, axis=1)
        data_df2 = data_df2.sum(axis = 1)
        data_df2 = data_df2.sort_values(ascending=False)
        df3 = data_df2[1:21]
        df4 = [i for i in df3.index]
        return df4


